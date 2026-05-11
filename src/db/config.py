import os
import re
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

INJECTION_PATTERNS = [
    r"ignore (all |previous |above |prior )?(instructions|rules|prompts|context)",
    r"you are now",
    r"new instructions",
    r"system prompt",
    r"forget (everything|all|what)",
    r"disregard",
    r"act as",
    r"jailbreak",
]