# 💪 FitFusion AI

FitFusion AI is an AI-powered fitness planning application that generates personalized workout and diet plans based on user profiles using Google Gemini AI.

It provides structured workout plans, Indian diet suggestions, and downloadable PDF reports via a Streamlit web application.

---

## 🚀 Live Demo

🔗 https://aicte-batch1-personalized-workout-and-diet-planner-with-ai-xbb.streamlit.app

---

## ✨ Features

- AI-based personalized fitness plans  
- Workout recommendations based on goals  
- Indian diet planning  
- Budget-friendly food suggestions  
- Daily calorie estimation  
- PDF report generation  
- Simple and interactive Streamlit UI  

---

## 🧠 Tech Stack

- Python  
- Streamlit  
- Google Gemini AI  
- ReportLab  
- python-dotenv  

---

## 📁 Project Structure

```text
FitFusion-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
└── utils/
    ├── ai_engine.py
    └── pdf_generator.py

⚙️ How to Run Locally
1. Install dependencies
Bash
pip install -r requirements.txt

2. Create environment variables
Create a .env file in the project root directory and add:

Code snippet
GEMINI_API_KEY=YOUR_API_KEY_HERE
A .env.example file is included for reference.

3. Run the application
Bash
streamlit run app.py
🧩 How It Works
User enters personal fitness details

Data is sent to Google Gemini AI

AI generates a personalized workout and diet plan

Output is displayed in Streamlit UI

A downloadable PDF report is generated

📌 Notes
.env.example is included as a template for environment setup

.env file is NOT uploaded for security reasons

venv folder is excluded from repository

Only required project files are included

Project is deployed using Streamlit Cloud

👨‍💻 Author
Rakshita Saxena

🔧 Built With
Python • Streamlit • Google Gemini AI • ReportLab
