from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import hashlib

def scrollPage(driver):
    SCROLL_PAUSE_TIME = 1.0

    curr_height = 0
    screen_height = driver.execute_script("return window.screen.height")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(arguments[0], arguments[0]+arguments[1]);", curr_height, screen_height)
        curr_height += screen_height/2

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        max_height = driver.execute_script("return document.body.scrollHeight")
        if curr_height >= max_height:
            break

class ShopeeProductDetailScanner:
    start_url = 'https://shopee.sg/OnePlus-Ace-5G-Gaming-Phone-Dual-Charger-(150W-SG-3-Pin-65W-)-SG-1-Year-Local-Warranty-i.93785607.9759889784?sp_atk=19284016-eb12-4474-bd23-6b3e00d8da53&xptdk=19284016-eb12-4474-bd23-6b3e00d8da53'

    def getDetails(self):
        chrome_options = Options()
        chrome_options.page_load_strategy = "eager"
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(self.start_url)

        scrollPage(driver)

        file_ref = f'{hashlib.sha224(b"{self.start_url}").hexdigest()}.html'
        html_file = open(file_ref, 'w')
        html_file.write(driver.page_source)
        html_file.close()

        with open(file_ref) as fp:
            soup = BeautifulSoup(fp, "html.parser")

            divs = soup.find_all(attrs={"class":"shopee-product-rating"})
            for div in divs:
                user_name = div.find(attrs={"class": "shopee-product-rating__author-name"}).string
                purchase_detail = div.find(attrs={"class": "shopee-product-rating__time"}).string
                variant = ''
                review_date = ''
                review_div = div.find(attrs={"class": "Em3Qhp"})
                review = review_div.string if review_div is not None else ""
                print(user_name, variant, review_date, review)

        driver.quit()

class LazadaProductDetailScanner:
    start_url = 'https://www.lazada.sg/products/lulufurnituresgdesigner-dining-chair-with-comfort-arm-rest-back-rest-price-including-delivery-i1239262907-s5066923000.html?spm=a2o42.home.flashSale.4.654346b52ETREX&search=1&mp=1&c=fs&clickTrackInfo=rs%3A0.1067863404750824%3Bfs_item_discount_price%3A19.90%3Bitem_id%3A1239262907%3Bmt%3Ahot%3Bfs_utdid%3A-1%3Bfs_item_sold_cnt%3A12%3Babid%3A287818%3Bfs_item_price%3A38.90%3Bpvid%3Adb52d104-e526-495e-80c6-dbc11e78d086%3Bfs_min_price_l30d%3A0%3Bdata_type%3Aflashsale%3Bfs_pvid%3Adb52d104-e526-495e-80c6-dbc11e78d086%3Btime%3A1658672170%3Bfs_biz_type%3Afs%3Bscm%3A1007.17760.287818.%3Bchannel_id%3A0000%3Bfs_item_discount%3A49%25%3Bcampaign_id%3A182337&scm=1007.17760.287818.0'

    def getDetails(self):
        chrome_options = Options()
        chrome_options.page_load_strategy = "eager"
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(self.start_url)
        
        scrollPage(driver)

        file_ref = f'{hashlib.sha224(b"{self.start_url}").hexdigest()}.html'
        html_file = open(file_ref, 'w')
        html_file.write(driver.page_source)
        html_file.close()

        with open(file_ref) as fp:
            soup = BeautifulSoup(fp, "html.parser")

            reviews_div = soup.find(attrs={"class":"mod-reviews"})
            review_items = reviews_div.find_all(attrs={"class":"item"})
            for review_item in review_items:
                review_date = review_item.find(attrs={"class": "top"}).find(attrs={"class": "title right"}).string
                user_name = review_item.find(attrs={"class": "middle"}).find_all('span')[0].string.replace("by ", "")
                review = review_item.find(attrs={"class": "item-content"}).find(attrs={"class": "content"}).string
                purchase_detail = review_item.find(attrs={"class":"skuInfo"}).string
                print(user_name, review_date, review, purchase_detail)
                
        
        driver.quit()

LazadaProductDetailScanner().getDetails()