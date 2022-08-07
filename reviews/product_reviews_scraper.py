from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import hashlib
from utilities.html_doc_scroller import HTMLDocumentScroller
from reviews.reviews_parser import ReviewsParser

class ReviewsScraper:
    start_url: str
    parser: ReviewsParser
    
    def __init__(self, start_url: str, parser: ReviewsParser):
        self.start_url =  start_url
        self.parser = parser

    def save_to_file(self, file_ref: str, driver: webdriver.Chrome):
        html_file = open(file_ref, 'w')
        html_file.write(driver.page_source)
        html_file.close()

    def request(self):
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
        [print(review.author, review.review, review.reviewed_at, review.meta, "\n") for review in reviews]

        # Close the web driver
        driver.quit()