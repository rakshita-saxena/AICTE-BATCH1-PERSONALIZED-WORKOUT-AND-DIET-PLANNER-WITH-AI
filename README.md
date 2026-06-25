# 💪 FitFusion AI

FitFusion AI is an AI-powered fitness planning application that generates personalized workout and diet plans based on user profiles using Google Gemini AI.

It provides structured workout plans, Indian diet suggestions, and downloadable PDF reports via a Streamlit web app.

---

## 🚀 Features

* AI-based personalized fitness plans
* Workout recommendations based on goals
* Indian diet planning
* Budget-friendly food suggestions
* Daily calorie estimation
* PDF report generation
* Simple Streamlit UI

---

## 🧠 Tech Stack

* Python
* Streamlit
* Google Gemini AI
* ReportLab
* python-dotenv

---

## 📁 Project Structure

FitFusion-AI/

├── app.py
├── requirements.txt
├── README.md
├── .env.example

└── utils/
    ├── ai_engine.py
    └── pdf_generator.py

---

## ⚙️ How to Run

Install dependencies:

pip install -r requirements.txt

Create a `.env` file in the project root directory and add your Gemini API key:

GEMINI_API_KEY=YOUR_API_KEY_HERE

A sample `.env.example` file is included in this repository for reference.

Run the app:

streamlit run app.py

---

## 🧩 How It Works

* User enters fitness details
* Data sent to Gemini AI
* AI generates plan
* Plan shown in UI
* PDF report generated

---

## 📌 Notes

* `.env.example` is provided as a template for environment configuration
* The actual `.env` file is NOT uploaded because it contains sensitive API keys
* `venv` folder is excluded from the repository
* Only required project files are uploaded
* Project uploaded using manual GitHub drag & drop method

---

## 👨‍💻 Author

Rakshita Saxena

---

## 🔧 Built With

Python, Streamlit, Google Gemini AI, ReportLab
