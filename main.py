from selenium import webdriver
from analyzer import Analyzer
import time
import json
import datetime

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Development/chromedriver"
TWITTER_EMAIL = "test.ithulin@yahoo.com"
TWITTER_PASSWORD = "E7354qb7hfv4T4v"


class InternetSPeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.down = int
        self.up = int
        self.ping = int
        self.now = datetime.datetime.now()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)

        self.driver.find_element_by_css_selector(".start-button a").click()
        time.sleep(55)

        self.ping = self.driver.find_element_by_css_selector(".ping-speed").text
        self.down = self.driver.find_element_by_css_selector(".download-speed").text
        self.up = self.driver.find_element_by_css_selector(".upload-speed").text

    def save_data(self):
        self.now = datetime.datetime.now()

        new_data = {
            f'{str(self.now.strftime("%Y-%m_%d %H:%M:%S"))}': {
                "ping": f"{self.ping}",
                "download": f"{self.down}",
                "upload": f"{self.up}"
            }
        }

        with open('Internet_speed_data.json', 'r+') as file:
            data = json.load(file)
            data.update(new_data)
            file.seek(0)
            json.dump(data, file)

        print(f'{self.now.strftime("%Y-%m_%d %H:%M:%S")}')
        print(f"Ping: {self.ping}, Download: {self.down}, Upload:{self.up}.")


bot = InternetSPeedTwitterBot()
while True:
    bot.get_internet_speed()
    bot.save_data()
    time.sleep(240)


# brain = Analyzer()
# brain.preprocess_data()
# print(brain.dataset_ordered)

