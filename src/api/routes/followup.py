from fastapi import APIRouter

from services.followup import FollowupService

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
async def generate(user_context: str, target_context: str):
    followup_message = followup_service.run(
        about_user_json=user_context, 
        about_target_json=target_context
    )
    return {"followup_message": followup_message}

@router.post("/regenerate")
async def regenerate():
    #TODO: Implement regenerate logic given consolidated user + feedback
    return {"message": "Regenerating followup content based on feedback..."}