# https://ru.hexlet.io/courses/python-polymorphism/lessons/dependency-inversion/exercise_unit

# https://ru.hexlet.io/code_reviews/1146490

# Python: Полиморфизм
# 9. Инверсия зависимостей

'''
Создайте полноценное консольное приложение, которое показывает текущую
погоду в городе.
'''

import argparse
import requests
from weather_service import WeatherService


def main(city_name):
    # BEGIN (write your solution here)
    weather_app = WeatherService(requests)
    response = weather_app.look_up(city_name)
    temperature = response['temperature']
    return f'Temperature in {city_name}: {temperature}C'
    # END


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', type=str, required=True)
    args = parser.parse_args()
    print(main(args.city))
