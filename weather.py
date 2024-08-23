import requests
from config import WEATHER_API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()
        
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        
        return f"The current weather in {city} is {description} with a temperature of {temp}°C."
    except requests.RequestException as e:
        print(f"Error fetching weather information: {str(e)}")
        return f"Sorry, I couldn't fetch the weather information for {city}. Please try again later."