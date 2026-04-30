from fastapi import APIRouter

from src.models.followup import FollowupModel
from src.services.followup import FollowupService
from db.queries.read import followup_contexts_query
from db.queries.write import save_followup_query

router = APIRouter()
followup_service = FollowupService()

@router.get("/")
async def root():
    return {
        "service": "Follow-up Message Generator",
        "description": "Generates AI-powered follow-up messages to maintain professional relationships and continue conversations.",
        "endpoints": ["/followup/generate", "/followup/regenerate"]
    }
    
@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/generate")
async def generate(user_id: str, contact_id: str):
    user_context, target_context = followup_contexts_query(user_id, contact_id)

    followup_response = followup_service.run(
        about_user_json=user_context, 
        about_target_json=target_context
    )

    try:
        followup_json = followup_response.json()
    except Exception as e:
        print("Error parsing follow-up response:", e)
        followup_json = {}

    print("Generated Follow-up Response:", followup_response)
    print("Follow-up JSON:", followup_json)

    followup = FollowupModel(
        user_id=user_id,
        contact_id=contact_id,
        status="draft", # Initial status should always be "draft"

        draft_message=followup_json.get("draft_message"),
        scheduled_for=followup_json.get("scheduled_for"),
        ai_reasoning=followup_json.get("ai_reasoning")
    )
    save_followup_query(followup)


@router.post("/regenerate")
async def regenerate():
    #TODO: Implement regenerate logic given consolidated user + feedback
    return {"message": "Regenerating followup content based on feedback..."}

# TESTING ENDPOINT WITH STATIC CONTEXTS
@router.get("/test/generate")
async def test_generate(user_context: str, target_context: str):
    
    followup_response = followup_service.run(
        about_user_json=user_context, 
        about_target_json=target_context
    )    
    
    return {"followup_response": followup_response}
