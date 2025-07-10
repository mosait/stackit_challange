from fastapi import FastAPI, HTTPException
from models import Notification
from messenger import forward_notification

app = FastAPI()

@app.post("/notify")
async def notify(notification: Notification):
    if notification.Type == "Warning":
        forward_notification(notification)
        return {"status": "forwarded"}
    return {"status": "ignored"}
