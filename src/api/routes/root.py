from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the Outreach Engine API"}

@router.get("/health")
async def health_check():
    return {"status": "ok"}
