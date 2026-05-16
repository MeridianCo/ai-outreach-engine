from fastapi import APIRouter, Depends

from src.models.followup import FollowupModel
from src.services.followup import FollowupService

from src.api.middleware.auth import get_current_user
from src.db.queries.read import get_followup_contexts
from src.db.queries.write import save_followup
from src.utils.ai_parser import convert_to_json

router = APIRouter()
followup_service = FollowupService()
    
@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/generate")
async def generate(contact_id: str, user_id: str = Depends(get_current_user)):
    user_context, target_context = get_followup_contexts(user_id, contact_id)

    followup_response = followup_service.run(
        about_user_json=user_context, 
        about_target_json=target_context
    )

    try:
        followup_json = convert_to_json(followup_response)
    except Exception as e:
        print("Error parsing follow-up response:", e)
        return {"error": "Failed to parse follow-up response"}

    followup = FollowupModel(
        user_id=user_id,
        contact_id=contact_id,
        status="draft", # Initial status should always be "draft"
        draft_message=followup_json.get("draft_message"),
        scheduled_for=followup_json.get("scheduled_for"),
        ai_reasoning=followup_json.get("ai_reasoning")
    )

    try:
        save_followup(followup)
    except Exception as e:
        print("Error saving follow-up to database:", e)
        return {"error": "Failed to save follow-up to database"}
    
    return {"followup": followup}

# TESTING ENDPOINT WITH STATIC CONTEXTS
@router.get("/test/generate")
async def test_generate(user_context: str, target_context: str):
    followup_response = followup_service.run(
        about_user_json=user_context, 
        about_target_json=target_context
    )    
    return {"followup_response": followup_response}
