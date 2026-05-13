import os
import sys
from datetime import datetime
from weather import get_weather_data
from messages import get_outfit_recommendation
from slack import send_slack_message

def main():
    print(f"🚀 Outfit Recommendation Bot started at {datetime.now()}")
    
    city = os.environ.get("CITY", "Seoul")
    
    try:
        # 1. 날씨 데이터 수집
        weather_data = get_weather_data(city)
        print(f"📍 Weather data collected for {city}")
        
        # 2. 의상 추천 멘트 생성
        recommendation = get_outfit_recommendation(weather_data)
        print(f"💬 Generated message: {recommendation}")
        
        # 3. 슬랙 발송
        success = send_slack_message(recommendation)
        
        if success:
            print("🎉 Process completed successfully.")
        else:
            print("⚠️ Process finished with Slack error.")
            
    except Exception as e:
        error_msg = f"❌ Outfit Bot Error: {str(e)}"
        print(error_msg)
        send_slack_message(error_msg)
        sys.exit(1)

if __name__ == "__main__":
    main()
