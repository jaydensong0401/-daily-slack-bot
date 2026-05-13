import requests
import os

def get_weather_data(city="Seoul"):
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("OPENWEATHER_API_KEY environment variable is not set.")
    
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
