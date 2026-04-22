import json
from pathlib import Path
from gemini import GeminiAgent

BASE_DIR = Path(__file__).parent
prompts_directory = BASE_DIR / "prompts" / "instruction.txt"

class FollowupService: # Eventually going to take a profile id and derive the context from the db
    def __init__(self):
        self.agent = GeminiAgent()

    def run(self, about_user_json: str, about_target_json: str) -> str:
        instruction = Path(prompts_directory).read_text().strip()

        # Turn json contextes into readable format
        user_context = json.loads(about_user_json)
        target_context = json.loads(about_target_json)
        user_context_str = "\n".join(f"{k}: {v}" for k, v in user_context.items())
        target_context_str = "\n".join(f"{k}: {v}" for k, v in target_context.items())
        
        return self.agent.generate_content(user_context_str, target_context_str, instruction)
