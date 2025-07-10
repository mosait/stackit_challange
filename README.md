# STACKIT Coding Challenge

## Overview
A simple FastAPI web service that receives JSON notifications via POST. 
Only `"Warning"` notifications are forwarded (simulated via console log). 
The message that are forwarded will also be send to Discord.

## Usage
- Create a ".env" and add:
```
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/..."
```
- Start API: `uvicorn main:app --reload`
- Send POST to `/notify` with JSON body
- Test: `pytest`
- Send Test manually via Terminal:
```
curl -X POST http://127.0.0.1:8000/notify \
     -H "Content-Type: application/json" \
     -d '{
           "Type": "Warning",
           "Name": "Backup Failure",
           "Description": "Database crash"
         }'
--- OR ---
curl -X POST http://127.0.0.1:8000/notify \
     -H "Content-Type: application/json" \
     -d '{
           "Type": "Info",
           "Name": "Quota Exceeded",
           "Description": "Compute limit hit"
         }'
```

- Test via Docs UI (/notify): 
```
1. http://127.0.0.1:8000/docs

2. Click on "Try it Out"

3. Navigate to /notify

4. Put in:
{
  "Type": "Warning",
  "Name": "Memory Leak",
  "Description": "High RAM usage"
}
--- OR ---
{
  "Type": "Info",
  "Name": "Quota Exceeded",
  "Description": "Compute limit hit"
}

5. Click Execute

6. See Result in the Terminal
```

## Dependencies
- Python 3.10+
- FastAPI
- pytest (optional)
