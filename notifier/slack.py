import requests
import os

def send_slack_message(message):
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("❌ Error: SLACK_WEBHOOK_URL environment variable not set.")
        return None
        
    response = requests.post(webhook_url, json={"text": message})
    
    if response.status_code == 200:
        print(f"✅ Success!")
    else:
        print(f"❌ Failed (Code: {response.status_code})")
        print(f"   Error: {response.text}")
    
    return response
