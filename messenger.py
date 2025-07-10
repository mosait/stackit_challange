from dotenv import load_dotenv
import os
import requests

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")    

def forward_notification(notification):
    message = f"⚠️ **Warning**\n**Name:** {notification.Name}\n**Description:** {notification.Description}"

    data = {
        "content": message
    }

    response = requests.post(DISCORD_WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("Forwarded to Discord successfully.")
    else:
        print(f"Failed to send message to Discord: {response.status_code}, {response.text}")
