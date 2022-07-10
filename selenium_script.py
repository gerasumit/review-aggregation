from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

def scrollPage(driver):
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

XIAOMI_TV_URL = 'https://shopee.sg/OnePlus-Ace-5G-Gaming-Phone-Dual-Charger-(150W-SG-3-Pin-65W-)-SG-1-Year-Local-Warranty-i.93785607.9759889784?sp_atk=19284016-eb12-4474-bd23-6b3e00d8da53&xptdk=19284016-eb12-4474-bd23-6b3e00d8da53'

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
start_url = XIAOMI_TV_URL
driver.get(start_url)

time.sleep(5)

scrollPage(driver)

html_file = open("phone_charger.html", "w")
html_file.write(driver.page_source)
html_file.close()

with open('phone_charger.html') as fp:
    soup = BeautifulSoup(fp, "html.parser")

    divs = soup.find_all(attrs={"class":"shopee-product-rating"})
    for div in divs:
        author_name = div.find(attrs={"class": "shopee-product-rating__author-name"}).string
        purchase_detail = div.find(attrs={"class": "shopee-product-rating__time"}).string
        review_div = div.find(attrs={"class": "Em3Qhp"})
        review = review_div.string if review_div is not None else ""
        print(author_name, purchase_detail, review)



driver.quit()
