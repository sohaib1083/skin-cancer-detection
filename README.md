# Skin Cancer Detection App 🔬

A full-stack web application using a fine-tuned **Vision Transformer (ViT)** model for skin lesion classification, backed by **Groq LLM** for AI-generated medical recommendations.

---

## 🏗️ Architecture

| Layer     | Technology                                   |
|-----------|----------------------------------------------|
| Backend   | FastAPI (Python)                             |
| Model     | ViT (`google/vit-base-patch16-224`, 7-class) |
| LLM       | Groq API — `llama-3.3-70b-versatile`         |
| Frontend  | Static HTML/CSS served by FastAPI            |
| Port      | `8000`                                       |

---

## 📁 Project Structure

```
VIT-skin-cancer/
├── app.py                     # FastAPI backend (model inference + LLM + static serving)
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (GROQ_API_KEY)
├── models/
│   └── vit_skin_cancer.pth   # Fine-tuned ViT model weights
└── static/                   # Frontend HTML pages served by FastAPI
    ├── index.html
    ├── new-scan.html
    ├── diagnosis-result.html
    ├── dashboard.html
    ├── patient-history.html
    ├── medical-report.html
    ├── classification-scan.html
    ├── emergency-scan.html
    ├── login.html
    ├── register.html
    └── css/
        └── styles.css
```

---

## 🚀 Running the Application

### Prerequisites

- Python 3.10+
- A valid [Groq API key](https://console.groq.com/)

### 1. Clone and enter the project

```bash
git clone https://github.com/sohaib1083/skin-cancer-detection.git
cd skin-cancer-detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the `.env` file

```bash
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```

Or create `.env` manually:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Start the server

```bash
uvicorn app:app --reload --port 8000
```

> The model (`vit_skin_cancer.pth`) loads at startup — this may take a few seconds.

### 5. Open the app

| URL                                      | Description                      |
|------------------------------------------|----------------------------------|
| http://localhost:8000                    | Web UI (redirects to index page) |
| http://localhost:8000/static/index.html  | Home page                        |
| http://localhost:8000/docs               | Interactive API docs (Swagger UI)|
| http://localhost:8000/redoc              | ReDoc API reference              |

---

## 🧪 Testing

### Quick health checks

```bash
# Root redirect (should return HTTP 307)
curl -o /dev/null -w "%{http_code}\n" http://localhost:8000/

# Static home page (should return HTTP 200)
curl -o /dev/null -w "%{http_code}\n" http://localhost:8000/static/index.html

# API docs (should return HTTP 200)
curl -o /dev/null -w "%{http_code}\n" http://localhost:8000/docs
```

### Test the `/predict` endpoint

```bash
curl -X POST http://localhost:8000/predict \
  -F "file=@/path/to/skin_lesion.jpg"
```

**Example response:**

```json
{
  "class_name": "Melanoma",
  "label": "mel",
  "confidence": 94.3,
  "risk_level": "High",
  "is_malignant": true,
  "prevention_steps": "AI-generated dermatology advice from Groq LLM..."
}
```

You can also test interactively via the Swagger UI at **http://localhost:8000/docs**.

---

## 📋 How It Works

1. **Upload Image** — User uploads a skin lesion photo through the web UI
2. **ViT Inference** — The fine-tuned ViT model classifies the image into one of 7 lesion types
3. **LLM Consultation** — The diagnosis label is sent to Groq's `llama-3.3-70b-versatile` model
4. **Medical Advice** — LLM returns prevention steps and treatment recommendations
5. **Display Results** — Both classification results and AI advice are shown to the user

### Supported Lesion Classes

| Label   | Class Name                    | Risk     | Malignant |
|---------|-------------------------------|----------|-----------|
| `mel`   | Melanoma                      | High     | ✅ Yes    |
| `bcc`   | Basal cell carcinoma          | High     | ✅ Yes    |
| `akiec` | Actinic keratoses             | Moderate | ❌ No     |
| `vasc`  | Vascular lesions              | Moderate | ❌ No     |
| `nv`    | Melanocytic nevi              | Low      | ❌ No     |
| `bkl`   | Benign keratosis-like lesions | Low      | ❌ No     |
| `df`    | Dermatofibroma                | Low      | ❌ No     |

---

## 📝 API Reference

### `POST /predict`

Classify a skin lesion image.

| Field              | Type    | Description                                |
|--------------------|---------|--------------------------------------------|
| `class_name`       | string  | Human-readable diagnosis                   |
| `label`            | string  | Short lesion code (e.g. `mel`, `nv`)       |
| `confidence`       | float   | Model confidence in % (0–100)              |
| `risk_level`       | string  | `Low`, `Moderate`, or `High`               |
| `is_malignant`     | boolean | Whether the lesion is malignant            |
| `prevention_steps` | string  | LLM-generated medical recommendations     |

### `GET /`

Redirects to `/static/index.html`.

### `GET /docs`

Interactive Swagger UI for exploring all endpoints.

---

## 🔧 Dependencies

```
fastapi
uvicorn
pillow
torch
torchvision
python-multipart
groq
python-dotenv
transformers
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Disclaimer

This application is an AI-assisted tool for **educational and research purposes only**. It is **not a substitute for professional medical diagnosis**. Always consult a licensed dermatologist for any skin concerns.
