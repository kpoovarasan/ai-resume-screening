🤖 AI Resume Screening System

An intelligent AI-powered Resume Screening System that analyzes resumes using Transformer-based NLP models and matches them against job descriptions to identify skill relevance, match score, and skill gaps.

This project is designed for HR automation, ATS systems, and AI/ML portfolio demonstration.

🚀 Features

📄 Resume upload (PDF/DOCX)

🧾 Job description input

🤖 AI-based skill extraction

📊 Resume–Job match score calculation

✅ Matched skills identification

❌ Missing skills detection

⚡ Fast and user-friendly web interface

🔐 Secure API key handling using environment variables

🛠️ Tech Stack
Frontend

HTML5

CSS3 (Responsive, Centered UI)

Backend

Python

Flask

AI / NLP

Transformer-based embeddings (Sentence-BERT)

Google Gemini API (for skill generation)

Cosine Similarity

Tools & Libraries

sentence-transformers

scikit-learn

nltk

python-dotenv

PyPDF2 / docx

Git & GitHub

📁 Project Structure
ai-resume-screening/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── home.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── images/
│
└── utils/
    ├── text_extractor.py
    ├── preprocess.py
    ├── similarity.py
    └── gemini_skill_generator.py
