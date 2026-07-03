import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def chat_with_dataset(summary, question):

    prompt = f"""
You are an AI Data Analyst.

Dataset Summary:

{summary}

User Question:
{question}

Answer the question based only on the dataset summary.
Use simple English.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"
    