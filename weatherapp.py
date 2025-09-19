from geopy.geocoders import Nominatim
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
from datetime import datetime

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

geolocator = Nominatim(user_agent="Weather App")

class WeatherFeatcher:
    def __init__(self):
        self.weather_api = "https://api.open-meteo.com/v1/forecast"
        self.weather_map = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snowfall",
            73: "Moderate snowfall",
            75: "Heavy snowfall",
            80: "Rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            95: "Thunderstorm",
            96: "Thunderstorm with hail",
            99: "Severe thunderstorm with hail"
        }


    def get_location(self, city):
        location = geolocator.geocode(city)
        if location is None:
            raise ValueError(f"City '{city}' not found. Please check spelling.")
        return location.latitude, location.longitude

    def get_weather(self, latitude, longitude):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": ["temperature_2m", "weathercode"],
        }
        responses = openmeteo.weather_api(self.weather_api, params=params)
        response = responses[0]

        current = response.Current()
        temp = current.Variables(0).Value()
        weathercode = current.Variables(1).Value()

        condition = self.weather_map.get(weathercode, "Unknown")

        return {
            "Temperature": temp, 
            "Condition": condition
            }


def main_app():
    print("Weather Fetcher using Open-Meteo")
    while True:
        city = str(input("Type a City (or 'x' to quit): ")).lower()
        if city == 'x':
            break
        try:
            latitude, longitude = app.get_location(city)
            weather = app.get_weather(latitude, longitude)
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
            print(f"Temperature: {weather['Temperature']:.2f}°C")
            print(f"Condition: {weather['Condition']}")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Unexpected error: {e}")
        
app = WeatherFeatcher()
if __name__ == "__main__":
    main_app()