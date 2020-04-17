from flask import current_app
import requests


def weather_and_the_city(city_name):

	weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
	params = {
		'key': current_app.config['WEATHER_API_KEY'],
		'q': current_app.config['WEATHER_DEFAULT_CITY'],
		'format': 'json',
		'num_of_days': '3'
	}
	try:
		result = requests.get(weather_url, params = params)
		result.raise_for_status()
		weather = result.json()
		if 'data' in weather:
			if 'current_condition' in weather['data']:
				try:
					return weather['data']['current_condition'][0]
				except(IndexError, TypeError):
					return False
	except(requests.RequestExeption, ValueError):
		print('оу где сеть :-(')
		return False				
	return False


if __name__ == "__main__":
    weather = weather_and_the_city("Moscow,Russia")
    print(weather)
