import requests
import os

def send_slack_message(message):
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("❌ SLACK_WEBHOOK_URL is not set.")
        return False
        
    payload = {"text": message}
    
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print("✅ Slack message sent successfully.")
            return True
        else:
            print(f"❌ Failed to send Slack message: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error sending Slack message: {e}")
        return False
