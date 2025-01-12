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

#add tests
def get_temperature(weather):
    temp = weather["current"]["temp"]
    return temp

def get_humidity(weather):
    humidity = weather["current"]["humidity"]
    return humidity

def get_wind(weather):
    wind = weather["current"]["wind_speed"]
    return wind

def get_weather_icon(weather):
    icon = weather["current"]["weather"][0]["icon"]
    return icon

def get_weather_description(weather):   
    description = weather["current"]["weather"][0]["description"]
    return description

def get_weather_icon_url(weather):
    icon = weather["current"]["weather"][0]["icon"]
    