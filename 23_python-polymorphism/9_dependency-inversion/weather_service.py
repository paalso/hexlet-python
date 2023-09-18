import requests
class WeatherService():
# BEGIN (write your solution here)
    def __init__(self, weather_api) -> None:
        self.api = weather_api

    def look_up(self, city):
        # response = {'name': 'city'}
        city_prefix = f'cities/{city.lower()}'
        request_url = f'{self.api}{city_prefix}'
        response = requests.get(request_url)
        return response.json()
# END
