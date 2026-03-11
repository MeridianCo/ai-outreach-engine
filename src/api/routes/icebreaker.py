from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {
        "service": "Icebreaker Generator",
        "description": "Generates AI-powered conversation starters to begin engaging possible connections IRL.",
        "endpoints": ["/icebreaker/generate", "/icebreaker/regenerate"]
    }
    
@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/generate")
async def generate():
    #TODO: Implement generate logic given consolidated user
    return {"message": "Generating icebreaker content..."}

@router.post("/regenerate")
async def regenerate():
    #TODO: Implement regenerate logic given consolidated user + feedback
    return {"message": "Regenerating icebreaker content based on feedback..."}
