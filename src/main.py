from fastapi import FastAPI

app = FastAPI(title="Outreach Engine API")

@app.get("/")
async def root():
    return {"message": "Welcome to the Outreach Engine API"}