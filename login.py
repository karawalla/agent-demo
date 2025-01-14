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

def get_weather_for_city(city):
    api_key = os.environ.get("API_KEY")
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    data = response.json()

def get_ten_day_forecast(lat, lon):
    """
    Get a 10-day weather forecast for the specified latitude and longitude.
    
    Args:
        lat (float): Latitude of the location
        lon (float): Longitude of the location
        
    Returns:
        dict: JSON response containing 10-day forecast data
    """
    api_key = os.environ.get("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt=10&units=imperial&appid={api_key}"
    
    response = requests.get(url)
    data = response.json()
    return data
