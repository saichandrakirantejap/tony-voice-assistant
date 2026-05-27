"""
weather.py

Current weather via OpenWeatherMap API.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str = "Birmingham") -> str:
    """Fetch current weather for a city and return a spoken response."""
    if not API_KEY:
        return "Weather API key not configured."

    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "imperial"    # Fahrenheit
        }
        response = requests.get(BASE_URL, params=params, timeout=5)
        data = response.json()

        if data.get("cod") != 200:
            return f"Sorry, I couldn't find weather for {city}."

        description = data["weather"][0]["description"]
        temp = round(data["main"]["temp"])
        feels_like = round(data["main"]["feels_like"])
        city_name = data["name"]

        return (
            f"The weather in {city_name} is {description}, "
            f"{temp} degrees Fahrenheit, "
            f"feels like {feels_like} degrees."
        )

    except requests.RequestException:
        return "Sorry, I couldn't reach the weather service right now."
