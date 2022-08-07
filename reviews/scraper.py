from typing import List
from urllib.parse import urlparse
from hyperlink import URLParseError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import hashlib
from reviews.model import ProductReview
from utilities.html_doc_scroller import HTMLDocumentScroller
from reviews.parser import LazadaReviewsParser, ReviewsParser, ShopeeReviewsParser

class ReviewsScraper:
    start_url: str
    parser: ReviewsParser
    
    def __init__(self, start_url: str):
        self.start_url =  start_url
        hostname = urlparse(start_url).hostname
        if hostname == 'shopee.sg':
            self.parser = ShopeeReviewsParser()
        elif hostname == 'www.lazada.sg':
            self.parser = LazadaReviewsParser()
        else:
            print(hostname)
            raise URLParseError

    def save_to_file(self, file_ref: str, driver: webdriver.Chrome):
        html_file = open(file_ref, 'w')
        html_file.write(driver.page_source)
        html_file.close()

    def request(self) -> List[ProductReview]:
        # Configure webdriver
        options = Options()
        options.page_load_strategy = "eager"
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get(self.start_url)

        # Scroll entire page
        HTMLDocumentScroller().scrollDocToEnd(driver)

        # Save html content to html file
        file_ref = f'{hashlib.sha224(b"{self.start_url}").hexdigest()}.html'
        self.save_to_file(file_ref=file_ref, driver=driver)

        # Parse the saved html
        reviews = self.parser.parse(file_ref=file_ref)

        # Close the web driver
        driver.quit()

        return reviews