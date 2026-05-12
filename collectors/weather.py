import requests
import os
from datetime import datetime

def get_weather_data(city="Seoul"):
    api_key = os.environ.get("WEATHER_API_KEY")
    if not api_key:
        return "❌ Weather API Key가 설정되지 않았습니다."
        
    # 관악구 위도 및 경도
    lat = 37.4654
    lon = 126.9436
    
    # One Call API 호출 (시간별/일별 예보 포함)
    # 3.0 버전 사용 (결제 연동된 계정 필수)
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely&appid={api_key}&units=metric&lang=kr"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            # 1. 현재 날씨
            current = data['current']
            current_desc = current['weather'][0]['description']
            temp = current['temp']
            feels_like = current['feels_like']
            humidity = current['humidity']
            
            emoji = "🌡️"
            if "비" in current_desc: emoji = "☔"
            elif "구름" in current_desc: emoji = "☁️"
            elif "맑음" in current_desc: emoji = "☀️"
            elif "눈" in current_desc: emoji = "❄️"
            
            # 2. 시간별 예보 (향후 3시간 요약)
            hourly_forecast = ""
            for i in range(1, 4): 
                hour_data = data['hourly'][i]
                dt = datetime.fromtimestamp(hour_data['dt'])
                hour_str = dt.strftime("%H시")
                h_temp = round(hour_data['temp'], 1)
                h_desc = hour_data['weather'][0]['description']
                hourly_forecast += f"  - {hour_str}: {h_temp}°C ({h_desc})\n"
                
            # 3. 일별 예보 (내일~글피 요약)
            daily_forecast = ""
            for i in range(1, 4): 
                day_data = data['daily'][i]
                dt = datetime.fromtimestamp(day_data['dt'])
                day_str = dt.strftime("%m/%d")
                d_temp_min = round(day_data['temp']['min'], 1)
                d_temp_max = round(day_data['temp']['max'], 1)
                d_desc = day_data['weather'][0]['description']
                daily_forecast += f"  - {day_str}: {d_temp_min}°C / {d_temp_max}°C ({d_desc})\n"

            result = (
                f"{emoji} *오늘 서울 관악구 날씨 알려줄게!!*\n\n"
                f"*📍 오늘의 날씨 잘보고 옷, 우산 잘챙겨 입어!!*\n"
                f"• 오늘의 날씨는{current_desc}\n"
                f"• 밖 온도는 {temp}°C\n"
                f"• 체감 온도는 {feels_like}°C\n"
                f"• 습도는 {humidity}%\n\n"
                f"*🕒 3시간 뒤 날씨는 이래!!*\n"
                f"{hourly_forecast}\n"
                f"*📅 일별 예보 잘보고 우산 챙겨!!*\n"
                f"{daily_forecast}\n"
                f"오늘도 화이팅하자ㅏㅏ!!🍀"
            )
            return result
        else:
            return f"❌ 날씨 정보 수집 실패: {data.get('message')}"
    except Exception as e:
        return f"❌ 오류 발생: {e}"
