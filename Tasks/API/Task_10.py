"""
    TODO:
        1. Get Valid API From Yandex Weather.
        2. Get JSON Data From API.
        3. Display JSON Weather Data On HTML.

    PROBLEM:
        - Yandex API is forbidden, raising error 403.
        - Check URL & Follow instructions in
            https://yandex.ru/dev/weather/doc/dg/concepts/errors.html
"""

from pprint import pprint

import requests

API_KEY = 'cb1d0e3f-e88c-4ef5-8950-a22b67d7726c'
BASE_URL = "https://api.weather.yandex.ru/v2/informers?"


def get_weather(lat, lon):
    header = {'X-Yandex-API-Key': API_KEY}
    latitude = lat
    longitude = lon
    language = "en_US"
    URL = f'{BASE_URL}lat={latitude}&lon{longitude}&lang={language}'
    # sample _data= {
    #
    #           "fact": {
    #             "temp": 20,
    #             "feels_like": 21,
    #             "icon": "ovc",
    #             "condition": "overcast",
    #             "wind_speed": 2,
    #             "wind_gust": 5.9,
    #             "wind_dir": "n",
    #             "pressure_mm": 745,
    #             "pressure_pa": 994,
    #             "humidity": 83,
    #             "daytime": "d",
    #             "polar": False,
    #             "season": "summer",
    #             "obs_time": 1470214800
    #
    #         }}
    try:
        response = requests.get(URL, header)
        data = response.json()
        # pprint(data)

        temperature = data['fact']["temp"]
        feels_like = data['fact']["feels_like"]
        latitude = data['info']['lat']
        longitude = data['info']['lon']
        condition = data["condition"]
        pressure_mm = data["pressure_mm"]
        humidity = data["humidity"]
        wind_speed = data["wind_speed"]
        wind_gust = data["wind_gust"]
        wind_dir = data["wind_dir"]

        return print(f"Weather is {temperature} today for longitude {longitude} "
                     f"and latitude {latitude}. It feels like {feels_like}.")

        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return response


def main():
    lat = input("Enter latitude: ")
    lon = input("Enter longitude: ")
    get_weather(lat, lon)


main()
