import requests
import os

def get_weather_data(city="Seoul"):
    # 기존에 사용하던 WEATHER_API_KEY와 새로운 이름을 모두 지원하도록 수정
    api_key = os.environ.get("OPENWEATHER_API_KEY") or os.environ.get("WEATHER_API_KEY")
    if not api_key:
        raise ValueError("Weather API Key (OPENWEATHER_API_KEY or WEATHER_API_KEY) environment variable is not set.")
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=kr"
    
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Weather API failed with status code {response.status_code}: {response.text}")
    
    data = response.json()
    
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "weather_main": data["weather"][0]["main"],
        "description": data["weather"][0]["description"]
    }
