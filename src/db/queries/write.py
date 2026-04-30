from .. import supabase
from src.models.followup import FollowupModel

def save_followup(followup: FollowupModel) -> None:
    supabase.table("follow_ups").insert(followup.model_dump()).execute()