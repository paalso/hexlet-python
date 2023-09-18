#!/usr/bin/env python3

#scripts/weather.py
import argparse
from weather_service import WeatherService

API_URL = 'http://localhost:8080/api/v2/'


def main(city_name):
    # BEGIN (write your solution here)
    service = WeatherService(API_URL)
    response = service.look_up(city_name)
    temperature = response['temperature']
    return f'Temperature in {city_name}: {temperature}C'
    # END


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', type=str, required=True)
    args = parser.parse_args()
    print(main(args.city))
