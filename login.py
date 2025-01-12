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

def main():
    lat = "40.730610"
    lon = "-73.935242"
    data = get_weather(lat,lon)
    print(data)
    print(data["current"]["weather"][0]["main"])
    print(data["current"]["weather"][0]["description"])
    print(data["current"]["weather"][0]["icon"])
    print(data["current"]["temp"])
    print(data["current"]["feels_like"])
    print(data["current"]["humidity"])
    print(data["current"]["wind_speed"])
    print(data["current"]["wind_deg"])
    print(data["current"]["clouds"])
    print(data["current"]["pop"])
    