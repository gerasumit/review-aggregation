from time import sleep
from selenium import webdriver

class HTMLDocumentScroller:
    def scrollDocToEnd(self, driver: webdriver.Firefox):
        SCROLL_PAUSE_TIME = 1.0

        curr_height = 0
        screen_height = driver.execute_script("return window.screen.height")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(arguments[0], arguments[0]+arguments[1]);", curr_height, screen_height)
            curr_height += screen_height/2

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            max_height = driver.execute_script("return document.body.scrollHeight")
            if curr_height >= max_height:
                break