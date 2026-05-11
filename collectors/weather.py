import requests
import os

def get_weather_data(city="Seoul"):
    # GitHub Secrets에 등록할 WEATHER_API_KEY 사용
    api_key = os.environ.get("WEATHER_API_KEY")
    if not api_key:
        return "❌ Weather API Key가 설정되지 않았습니다."
        
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=kr"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            
            # 이모지 매칭
            emoji = "🌡️"
            if "비" in weather_desc: emoji = "☔"
            elif "구름" in weather_desc: emoji = "☁️"
            elif "맑음" in weather_desc: emoji = "☀️"
            elif "눈" in weather_desc: emoji = "❄️"
            
            result = (
                f"{emoji} *오늘의 서울 날씨 리포트*\n\n"
                f"• 상태: {weather_desc}\n"
                f"• 현재 온도: {temp}°C\n"
                f"• 체감 온도: {feels_like}°C\n"
                f"• 습도: {humidity}%\n"
            )
            return result
        else:
            return f"❌ 날씨 정보를 가져오지 못했습니다. (에러: {data.get('message')})"
    except Exception as e:
        return f"❌ 날씨 수집 중 오류 발생: {e}"
