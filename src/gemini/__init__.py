from pathlib import Path
from google import genai
from google.genai import types
from src.gemini.config import AGENT_ROLE, GEMINI_KEY, GEMINI_MODEL
class GeminiAgent:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_KEY)
        self.model = GEMINI_MODEL
        self.role = AGENT_ROLE
        
    def generate_content(self, user_context, target_context, instruction):
        system_prompt = ( 
            f"This is your role:{self.role}\n"
            f"\nThis is the relevant context about the user:\n{user_context} and"
            f"\nThis is the relevant context about the desired connection:\n{target_context}\n"
        )
        
        response = self.client.models.generate_content(
            model=self.model,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            ),
            contents=instruction
        )
        return response.text
            
    