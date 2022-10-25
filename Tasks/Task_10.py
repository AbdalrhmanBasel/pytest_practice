import requests
from bs4 import BeautifulSoup

request = requests.get("https://yandex.ru/pogoda/").text


def scrap_weather(request):
    soup = BeautifulSoup(request, 'html.parser')
    weather_of_week = soup.find_all(class_="forecast-briefly__day swiper-slide")
    return weather_of_week


print(scrap_weather(request))
