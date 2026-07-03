import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_insights(summary):
    """
    Generate AI insights using Gemini.
    """

    prompt = f"""
You are an expert Data Analyst.

Analyze the following dataset summary.

{summary}

Provide the following:

1. Dataset Overview
2. Key Insights
3. Missing Value Analysis
4. Outlier Analysis
5. Recommended Visualizations
6. Business Recommendations
7. Future Analysis Suggestions

Explain everything in simple English.
"""

    try:
        response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)

        return response.text

    except Exception as e:
        return f"Error: {e}"
    