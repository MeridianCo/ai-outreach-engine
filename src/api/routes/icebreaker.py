from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/generate")
async def generate():
    #TODO: Implement generate logic given consolidated user
    return {"message": "Generating icebreaker content..."}

