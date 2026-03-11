from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    {
    "service": "AI Outreach Engine API",
    "version": "1.0",
    "description": "Generates AI-powered outreach messages, icebreakers, and follow-ups for professional networking.",
    "endpoints": {
        "outreach": [
            "/outreach/generate",
            "/outreach/regenerate"
        ],
        "icebreaker": [
            "/icebreaker/generate",
            "/icebreaker/regenerate"
        ],
        "followup": [
            "/followup/generate",
            "/followup/regenerate"
        ],
        "health": [
            "/health"
        ]
    }
}

@router.get("/health")
async def health_check():
    return {"status": "ok"}
