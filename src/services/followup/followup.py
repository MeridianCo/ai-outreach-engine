import json
from pathlib import Path
from src.gemini import GeminiAgent

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

# FOR TESTING PURPOSES ONLY
if __name__ == "__main__":
    service = FollowupService()
    
    # Example context data (to be replaced by actual data from the db)
    sample_user_context = json.dumps({
        # User's own profile
        "user_name": "Tio",
        "user_role": "CS student & aspiring ML engineer",
        "user_experience": "Built 2 ML projects, interned at a fintech startup",
        "user_goals": "Break into AI product roles at mid-stage startups",

        # Follow-up history
        "platform": "LinkedIn",
        "followups_sent": 1,
        "last_followup_days_ago": 6
    })  
    sample_target_context = json.dumps({
        # Target's profile
        "target_name": "Sarah Chen",
        "target_role": "AI Product Lead at Series B startup",
        "target_company": "NovaMind AI",
        "target_context": "Recently posted about challenges in productizing LLMs, spoke at NeurIPS",

    })

    output = service.run(
        about_user_json=sample_user_context,
        about_target_json=sample_target_context
    )

    print(output)