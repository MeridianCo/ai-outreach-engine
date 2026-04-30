import json
import re

def sanitize_for_json(data: str) -> str:
    data = data.strip()
    data = re.sub(r"^```json", "", data).strip()
    data = re.sub(r"```$", "", data).strip()
    return data

def remove_emdashes(text: str) -> str:
    return text.replace("—", ", ")

def convert_to_json(data: str) -> dict:
    sanitized = sanitize_for_json(data)
    sanitized = remove_emdashes(sanitized)
    return json.loads(sanitized)