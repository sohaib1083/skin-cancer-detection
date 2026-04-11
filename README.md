# Skin Cancer Detection App 🔬

A full-stack application using Vision Transformer (ViT) for skin cancer detection, integrated with Groq LLM for medical recommendations.

## 🏗️ Architecture

### Backend (FastAPI)

- **Framework**: FastAPI
- **Model**: Vision Transformer (ViT) from Hugging Face Transformers
- **LLM Integration**: Groq API (llama-3.3-70b-versatile)
- **Port**: 8000

### Frontend (Next.js)

- **Framework**: Next.js 16.2.2 (with Turbopack)
- **UI**: React with Tailwind CSS
- **Port**: 3000

## 🚀 Running the Application

### Prerequisites

- Python 3.10+
- Node.js 18+
- Groq API Key (in `.env` file)

### 1. Start the Backend

```bash
cd /home/sohaib/Documents/projects/VIT-skin-cancer

# Activate virtual environment (if needed)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
.venv/bin/python -m uvicorn app:app --reload --port 8000
```

The API will be available at: **http://localhost:8000**

- API Documentation: http://localhost:8000/docs

### 2. Start the Frontend

```bash
cd cancer-detection-ui

# Install dependencies (first time only)
npm install

# Run Next.js dev server
npm run dev
```

The web app will be available at: **http://localhost:3000**

## 📋 How It Works

1. **Upload Image**: User uploads a skin lesion image through the web interface
2. **AI Prediction**: Image is sent to FastAPI backend
3. **ViT Analysis**: The trained ViT model classifies the lesion into one of 7 classes:
   - `bkl`: Benign keratosis-like lesions
   - `bcc`: Basal cell carcinoma
   - `akiec`: Actinic keratoses
   - `vasc`: Vascular lesions
   - `nv`: Melanocytic nevi
   - `mel`: Melanoma
   - `df`: Dermatofibroma
4. **LLM Consultation**: The diagnosis is sent to Groq's LLM
5. **Medical Advice**: LLM generates prevention steps and treatment recommendations
6. **Display Results**: Both the diagnosis and recommendations are shown to the user

## 🔧 Technical Details

### Backend Stack

- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `transformers` - Hugging Face model library
- `torch` - PyTorch deep learning framework
- `groq` - Groq API client
- `python-dotenv` - Environment variable management
- `pillow` - Image processing

### Frontend Stack

- Next.js 16.2.2
- React 19
- Tailwind CSS
- TypeScript

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## 📁 Project Structure

```
VIT-skin-cancer/
├── app.py                      # FastAPI backend
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
├── models/
│   └── vit_skin_cancer.pth    # Trained ViT model
└── cancer-detection-ui/       # Next.js frontend
    ├── app/
    │   ├── page.tsx           # Main UI component
    │   └── layout.tsx
    ├── package.json
    └── ...
```

## ✅ Testing

### Backend Health Check

```bash
curl http://localhost:8000/docs
```

### Frontend Health Check

```bash
curl http://localhost:3000
```

## 🎯 Features

- ✅ Image upload with preview
- ✅ Real-time skin cancer classification
- ✅ AI-generated medical recommendations
- ✅ Responsive UI with dark mode support
- ✅ CORS enabled for cross-origin requests
- ✅ Medical disclaimer for user safety

## ⚠️ Disclaimer

This is an AI-powered tool and should not replace professional medical advice. Always consult a dermatologist for proper diagnosis and treatment.

## 📝 API Endpoints

### POST /predict

Upload an image for skin cancer detection.

**Request:**

- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: `file` (image file)

**Response:**

```json
{
  "class_name": "Melanoma",
  "prevention_steps": "AI-generated recommendations..."
}
```

## 🛠️ Development

The application runs in development mode with hot-reload enabled:

- FastAPI auto-reloads on file changes
- Next.js uses Turbopack for fast refresh

## 📊 Status

✅ **Backend**: Running on http://localhost:8000
✅ **Frontend**: Running on http://localhost:3000
✅ **Model**: Loaded successfully
✅ **Groq LLM**: Configured and ready
