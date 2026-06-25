import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_fitness_plan(user_data):

    prompt = f"""
You are a professional certified fitness coach and nutrition expert.

Create a highly personalized workout and diet plan based on the user's profile.

User Details:
Name: {user_data['name']}
Age: {user_data['age']}
Gender: {user_data['gender']}
Height: {user_data['height']} cm
Weight: {user_data['weight']} kg
Goal: {user_data['goal']}
Food Preference: {user_data['food_pref']}
Budget: {user_data['budget']}

Generate the following sections:

1. Fitness Assessment
- Analyze the user's current fitness condition.
- Mention strengths and areas for improvement.

2. 7-Day Workout Plan (Monday to Sunday)
- Provide a complete weekly workout schedule.
- Include exercises, sets, reps, and duration.
- Include rest/recovery recommendations where needed.

3. Detailed Indian Diet Plan
For each day include:
Breakfast
Mid-Morning Snack
Lunch
Evening Snack
Dinner

4. Daily Calorie Recommendation
- Recommend daily calorie intake based on the user's goal.

5. Health Tips
- Hydration
- Sleep
- Recovery
- Healthy lifestyle practices

6. Motivation Section
- Encourage consistency and long-term healthy habits.

Budget Guidelines:

If Budget is LOW:
Recommend affordable foods such as dal, rice, roti, eggs, bananas, peanuts, soya chunks, milk, seasonal fruits, and vegetables.

If Budget is MEDIUM:
Include paneer, curd, chicken, fruits, nuts, and balanced meal options.

If Budget is HIGH:
Include premium protein sources, dry fruits, fish, supplements (optional), and greater meal variety.

IMPORTANT INSTRUCTIONS:

- The plan must be practical and realistic.
- Consider cultural food habits and locally available foods.
- Follow the selected food preference strictly.
- Ensure recommendations are budget-friendly.
- Personalize recommendations using age, height, weight, goal, food preference, and budget.
- Prefer foods commonly available in India.
- Avoid rare or difficult-to-find foods.
- Keep the response detailed and professional.
- Avoid unnecessary repetition.

OUTPUT FORMAT RULES:

- Return ONLY plain text.
- Do NOT use Markdown.
- Do NOT use ###, ##, **, *, -, or -- symbols.
- Do NOT use bullet points.
- Do NOT use tables.
- Use simple numbered section headings only.
- Keep formatting PDF-friendly.
- Use short paragraphs.
- Make the response clean and professional.

Example Format:

1. Fitness Assessment

Current Condition:
...

Strengths:
...

Areas for Improvement:
...

2. 7-Day Workout Plan

Monday:
...

Tuesday:
...

3. Detailed Indian Diet Plan

Breakfast:
...

Lunch:
...

4. Daily Calorie Recommendation

5. Health Tips

6. Motivation Section

The response will be directly converted into a PDF document.
Return clean plain text only.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"""
AI service is temporarily busy.

Please try again after a few moments.

Error:
{str(e)}
"""
