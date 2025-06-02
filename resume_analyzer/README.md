# Resume Analyzer

This project analyzes resumes and matches them with job descriptions.

## Setup

1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the backend:
   ```
   cd backend
   python -m flask run
   ```
4. Run the frontend:
   ```
   cd frontend
   python app.py
   ```
   # 🧠 AI-powered Resume Analyzer

This is a web-based application built using **Streamlit** that leverages **NLP models** to analyze resumes, extract relevant skills, and match them against job descriptions. It’s designed to help recruiters or job seekers evaluate resume fit using AI.

---

## 🚀 Features

- Upload and parse PDF resumes.
- Extract key skills and information from resumes using NLP.
- Match resumes against job descriptions.
- Streamlit-based intuitive UI.
- Modular project structure with a backend utility layer.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, Sentence-Transformers
- **NLP Models**: BERT-based SentenceTransformer
- **Others**: PyMuPDF for PDF parsing, NumPy, scikit-learn

---

## 📁 Project Structure

