import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routes
from src.api.routes import root_router

app = FastAPI(title="Outreach Engine API")

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(root_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

