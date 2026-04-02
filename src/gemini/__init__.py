import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

# Load Gemini API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Init Gemini client
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Write a poem about a sunset." # test prompt to test connection
)

print(response.text)