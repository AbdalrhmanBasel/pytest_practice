from bs4 import BeautifulSoup
import requests


def HTML_Parser():
    url = "https://yandex.ru/pogoda/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    info = soup.find("div", {"class": "new_info_next"})

    # All Source Code
    # print(soup.prettify())






if __name__ == "__main__":
    HTML_Parser()
