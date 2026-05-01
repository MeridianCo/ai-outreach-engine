import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

BASE_DIR = Path(__file__).parent
AGENT_ROLE = Path(BASE_DIR / "prompts" / "agent_role.txt").read_text().strip()

