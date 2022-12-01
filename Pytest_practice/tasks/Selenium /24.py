import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "chromedriver"


def launch_Browser():
    # SETUP
    browser = webdriver.Chrome(PATH)
    browser.get("https://yandex.ru/pogoda/")

    # Get Title Of The Page
    print("Website Title:", browser.title)

    # Get URL Of The Page
    print("Website URL:", browser.current_url)

    # Get Source Code
    # print(browser.page_source)

    # To Navigate To Previous Page
    # browser.back()

    # To Navigate To Next Page
    # browser.forward()

    # Check If Element Is Identified
    week_weather2 = browser.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[3]/ul')
    for day in week_weather2:
        print("Week's Weather: " + day.get_attribute('innerHTML'))
        print(50 * "#")

    # displayed = today_weather.is_displayed()
    # print(displayed)




    # Wait 60 seconds
    time.sleep(1000)

    # Close Tab In Browser
    browser.close()

    # Quit The Entire Browser
    browser.quit()


if __name__ == "__main__":
    launch_Browser()
