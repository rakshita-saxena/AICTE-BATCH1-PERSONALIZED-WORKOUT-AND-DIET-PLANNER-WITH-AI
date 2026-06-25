import streamlit as st
from utils.ai_engine import generate_fitness_plan
from utils.pdf_generator import create_pdf

# Page config
st.set_page_config(
    page_title="FitFusion AI",
    page_icon="💪",
    layout="wide"
)

# Header
st.title("💪 FitFusion AI")
st.subheader("Personalized Workout and Diet Planner with AI")

# Sidebar
st.sidebar.header("👤 User Profile")

name = st.sidebar.text_input("Enter Name")

age = st.sidebar.number_input(
    "Age",
    min_value=15,
    max_value=80,
    value=21
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

height = st.sidebar.number_input(
    "Height (cm)",
    min_value=100,
    max_value=250,
    value=170
)

weight = st.sidebar.number_input(
    "Weight (kg)",
    min_value=30,
    max_value=200,
    value=70
)

goal = st.sidebar.selectbox(
    "Fitness Goal",
    [
        "Weight Loss",
        "Weight Gain",
        "Muscle Gain",
        "Maintain Fitness"
    ]
)

food_pref = st.sidebar.selectbox(
    "Food Preference",
    [
        "Vegetarian",
        "Non-Vegetarian",
        "Vegan"
    ]
)

budget = st.sidebar.selectbox(
    "Budget",
    [
        "Low",
        "Medium",
        "High"
    ]
)

# Main Dashboard
st.header("📊 User Summary")

col1, col2 = st.columns(2)

with col1:
    st.write("### Personal Details")
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")

with col2:
    st.write("### Fitness Details")
    st.write(f"Height: {height} cm")
    st.write(f"Weight: {weight} kg")
    st.write(f"Goal: {goal}")

st.success("User information captured successfully!")

# AI Section
st.markdown("---")
st.header("🤖 AI Fitness Plan Generator")

st.info("Click the button below to generate your personalized AI fitness plan.")

if st.button("🚀 Generate AI Fitness Plan"):

    if name == "":
        st.error("Please enter your name first!")
    else:

        user_data = {
            "name": name,
            "age": int(age),
            "gender": gender,
            "height": float(height),
            "weight": float(weight),
            "goal": goal,
            "food_pref": food_pref,
            "budget": budget
        }

        with st.spinner("Generating your AI fitness plan... 🤖"):

            ai_response = generate_fitness_plan(user_data)

        st.success("AI Plan Ready!")

        st.markdown(ai_response)
        pdf_file = create_pdf(ai_response)

        st.download_button(
           label="📄 Download Fitness Plan PDF",
           data=pdf_file,
           file_name=f"{name}_Fitness_Plan.pdf",
           mime="application/pdf"
        )