from fastapi import FastAPI, HTTPException
from datetime import date, datetime

app = FastAPI(root_path="/api/v1")


@app.get("/")
async def root():
    return {"message": "Hello World"}

data = [
    {
        "campaign_id": 1,
        "name": "Summer Launch",
        "due_date": date(2025, 9, 1),
        "created_at": datetime.now(),
    },
    {
        "campaign_id": 2,
        "name": "Black Friday",
        "due_date": date(2025, 11, 28),
        "created_at": datetime.now(),
    },
]

@app.get("/campaigns/")
async def read_campaigns(id: int):
    return {"campaigns": data}

@app.get("/campaigns/{id}")
async def read_campaign(id: int):
    for campaign in data:
        if campaign.get("campaign_id") != id:
            raise HTTPException(status_code=404)
        return {"campaign": campaign}