from fastapi import FastAPI, HTTPException, Request
from datetime import date, datetime
import random

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

@app.get("/campaigns")
async def read_campaigns():
    return {"campaigns": data}

@app.get("/campaigns/{id}")
async def read_campaign(id: int):
    for campaign in data:
        if campaign.get("campaign_id") == id:
            return {"campaign": campaign}
    raise HTTPException(status_code=404)

@app.post("/campaigns", status_code=201)
async def create_campaign(request: Request):
    body = await request.json()
    new = {
        "campaign_id": random.randint(1000, 9999),
        "name": body.get("name"),
        "due_date": body.get("due_date"),
        "created_at": datetime.now(),
    }

    data.append(new)
    return {"campaign": new}


@app.put("/campaigns/{id}")
async def update_campaign(id: int, request: Request):
    body = await request.json()
    for index, campaign in enumerate(data):
        if campaign["campaign_id"] == id:
            updated = {
                "campaign_id": id,
                "name": body["name"],
                "due_date": body["due_date"],
                "created_at": datetime.now(),
            }
            data[index] = updated
            return {"campaign": updated}
    raise HTTPException(status_code=404)


@app.delete("/campaigns/{id}", status_code=204)
async def delete_campaign(id: int):
    for index, campaign in enumerate(data):
        if campaign["campaign_id"] == id:
            data.pop(index)
            return Response(status_code=204)
    raise HTTPException(status_code=404)