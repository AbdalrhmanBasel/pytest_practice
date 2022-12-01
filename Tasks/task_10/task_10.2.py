import requests
from bs4 import BeautifulSoup


class Parse_HTML:

    def get_content(self, request):
        soup = BeautifulSoup(request, 'html.parser')
        week = soup.find('ul', class_="swiper-wrapper").prettify()
        return week


    def parse_to_HTML(self, get_content):
        file = open('10.html', 'w', encoding='utf-8')
        file.write(str(get_content))
        file.close()


if __name__ == "__main__":
    request = requests.get("https://yandex.ru/pogoda/").text
    c1 = Parse_HTML()
    content = c1.get_content(request)
    c1.parse_to_HTML(content)
