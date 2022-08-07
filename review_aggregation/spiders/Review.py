import scrapy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from scrapy_selenium import SeleniumRequest
import time

XIAOMI_TV_URL = 'https://shopee.sg/OnePlus-Ace-5G-Gaming-Phone-Dual-Charger-(150W-SG-3-Pin-65W-)-SG-1-Year-Local-Warranty-i.93785607.9759889784?sp_atk=19284016-eb12-4474-bd23-6b3e00d8da53&xptdk=19284016-eb12-4474-bd23-6b3e00d8da53'

class ReviewSpider(scrapy.Spider):
    name = 'Review'

    def start_requests(self):
        yield SeleniumRequest(
            url = XIAOMI_TV_URL,
            wait_time = 3,
            screenshot = True,
            callback = self.parse,
            dont_filter = True
        )

    def parse(self, response):
        self.log(response.xpath('//title/text()').get())
        self.log(response.xpath('//div[@class="product-ratings__list"]').getall())

    def scrollPage(self, driver):
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
