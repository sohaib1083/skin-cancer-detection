from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image
import requests
import io
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Define a Pydantic model for the response
class PredictionResponse(BaseModel):
    class_name: str
    prevention_steps: str

# Load your trained VIT model from transformers
model = ViTForImageClassification.from_pretrained("google/vit-base-patch16-224", num_labels=7, ignore_mismatched_sizes=True)
model.load_state_dict(torch.load("./models/vit_skin_cancer.pth"))
model.eval()

# Load the image processor
processor = ViTImageProcessor.from_pretrained("google/vit-base-patch16-224")

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Groq client
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.post("/predict", response_model=PredictionResponse)
async def predict_image(file: UploadFile = File(...)):
    # Read the uploaded image
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    
    # Process the image using the ViT processor
    inputs = processor(images=image, return_tensors="pt")
    
    # Make the prediction
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = logits.argmax(-1).item()
    

    classes = ['bkl', 'bcc', 'akiec', 'vasc', 'nv', 'mel', 'df']
    class_names = {
        'bkl': 'Benign keratosis-like lesions',
        'bcc': 'Basal cell carcinoma',
        'akiec': 'Actinic keratoses',
        'vasc': 'Vascular lesions',
        'nv': 'Melanocytic nevi',
        'mel': 'Melanoma',
        'df': 'Dermatofibroma'
    }
    predicted_label = classes[predicted_class]
    class_name = class_names[predicted_label]
    
    # Get prevention steps from Groq LLM
    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a dermatology expert AI assistant. Provide clear, actionable prevention steps and medical advice for skin conditions."
                },
                {
                    "role": "user",
                    "content": f"A patient has been diagnosed with {class_name} ({predicted_label}). Provide prevention steps, treatment recommendations, and when they should consult a dermatologist. Keep the response concise and actionable."
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=500
        )
        prevention_steps = chat_completion.choices[0].message.content
    except Exception as e:
        prevention_steps = f"Unable to fetch prevention steps at this time. Please consult a dermatologist for personalized advice. Error: {str(e)}"
    
    return PredictionResponse(class_name=class_name, prevention_steps=prevention_steps)
