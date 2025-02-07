API_URL = 'http://localhost:8080/api/v2/'


class WeatherService():
    def __init__(self, http_client):
        self.http_client = http_client

    def look_up(self, city_name):
        url = f'{API_URL}cities/{city_name}'
        response = self.http_client.get(url)
        return response.json()
