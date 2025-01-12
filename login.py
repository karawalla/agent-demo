#code to get weather
import requests
import json
import time
import os

def get_weather(lat,lon):
    api_key = os.environ.get("API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}
    &exclude=minutely,hourly,alerts&units=imperial&appid={api_key}
    "
    response = requests.get(url)
    data = response.json()
    return data

def get_forecast(lat,lon):
    api_key = os.environ.get("API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}
    &lon={lon}
    &exclude=minutely,alerts&units=imperial&appid={api_key}
    "
    response = requests.get(url)
    data = response.json()
    return data

