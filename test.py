from google import genai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Read the API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found!")
    exit()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Test request
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello! Can you reply with 'Gemini is working!'?"
)

print(response.text)
