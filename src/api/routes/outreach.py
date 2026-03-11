from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {
        "service": "Outreach Message Generator",
        "description": "Generates AI-powered professional outreach messages for networking and connection requests.",
        "endpoints": ["/outreach/generate", "/outreach/regenerate"]
    }

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/generate")
async def generate():
    #TODO: Implement generate logic given consolidated user
    return {"message": "Generating outreach content..."}

@router.post("/regenerate")
async def regenerate():
    #TODO: Implement regenerate logic given consolidated user + feedback
    return {"message": "Regenerating outreach content based on feedback..."}
    



