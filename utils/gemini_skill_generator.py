
from google import genai
import os

# Create client (NEW SDK)
client = genai.Client(api_key=os.getenv("AIzaSyB2KfPXRzxAW2s1SkalVtAAKE-bulY3qvM"))


def generate_skills_from_role(role: str):
    prompt = f"""
You are an expert HR AI assistant.
Generate a concise comma-separated list of technical skills
required for the role: {role}.
Only skills, no explanation.
"""

    response = client.models.generate_content(
        model="models/gemini-flash-lite-latest",
        contents=prompt
    )

    skills_text = response.text.strip()
    return [s.strip().lower() for s in skills_text.split(",")]
