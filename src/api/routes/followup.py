from fastapi import APIRouter

from services.followup import FollowupService
from db.queries import followup_contexts_query

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

    followup_message = followup_service.run(
        about_user_json=user_context, 
        about_target_json=target_context
    )
    return {"followup_message": followup_message}

# TESTING ENDPOINT WITH STATIC CONTEXTS
@router.get("/test/generate")
async def test_generate(user_context: dict, target_context: dict):
    followup_message = followup_service.run(
        about_user_json=user_context, 
        about_target_json=target_context
    )
    return {"followup_message": followup_message}

@router.post("/regenerate")
async def regenerate():
    #TODO: Implement regenerate logic given consolidated user + feedback
    return {"message": "Regenerating followup content based on feedback..."}