from .. import supabase
from src.db.schema import FOLLOW_UPS_APP_WRITABLE
from src.models.followup import FollowupModel
from src.utils.ai_parser import validate_ai_response

def save_followup(followup: FollowupModel) -> None:
    raw = followup.model_dump()
    safe = validate_ai_response(raw, FOLLOW_UPS_APP_WRITABLE)
    supabase.table("follow_ups").insert(safe).execute()
    