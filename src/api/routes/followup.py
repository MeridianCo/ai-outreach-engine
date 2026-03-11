from fastapi import APIRouter

router = APIRouter()

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
async def generate():
    #TODO: Implement generate logic given consolidated user
    return {"message": "Generating followup content..."}

@router.post("/regenerate")
async def regenerate():
    #TODO: Implement regenerate logic given consolidated user + feedback
    return {"message": "Regenerating followup content based on feedback..."}

