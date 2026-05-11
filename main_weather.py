from collectors.weather import get_weather_data
from notifier.slack import send_slack_message
from datetime import datetime

def main():
    print(f"🌤️ Weather Bot started at {datetime.now()}")
    
    # 1. 날씨 데이터 가져오기
    weather_info = get_weather_data("Seoul")
    
    # 2. 슬랙으로 전송
    send_slack_message(weather_info)

if __name__ == "__main__":
    main()
