import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

@dataclass
class Weatherdata:
	main: str
	description: str
	icon: str
	wind_speed: float
	temp: float
	temp_feels: float


load_dotenv()
API_key = os.getenv('API_KEY')

def getlatlong(city_name,state_code,country_code,API_key):
	response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}").json()
	data = response[0]
	lat, long = data.get("lat"), data.get("lon")
	return lat, long

def getweather(lat, long, API_key, units):
	response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API_key}&units={units}").json()
	data = Weatherdata (
		main=response.get('weather')[0].get('main'),
		description=response.get('weather')[0].get('description'),
		icon=response.get('weather')[0].get('icon'),
		wind_speed=response.get('wind').get('speed'),
		temp=response.get('main').get('temp'),
		temp_feels=response.get('main').get('feels_like'),
	)
	return data

def main(city, state, country, measurement): # Valid measurements: Imperial or Metric
	lat, long = getlatlong(city, state, country, API_key)
	weather_data = getweather(lat, long, API_key, measurement)
	return weather_data