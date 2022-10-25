import hashlib
from typing import List
from product_links.parser import ProductLinkParser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from product_links.model import ProductLink
from utilities.html_doc_scroller import HTMLDocumentScroller
import os

class ProductLinkScraper:
    start_url: str
    parser: ProductLinkParser
    
    def __init__(self, start_url: str):
        self.start_url =  start_url
        self.parser = ProductLinkParser()

    def save_to_file(self, file_ref: str, driver: webdriver.Chrome):
        html_file = open(file_ref, 'w')
        html_file.write(driver.page_source)
        html_file.close()

    def request(self) -> List[ProductLink]:
        print(os.environ)

        # Get user agent
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        
        # Configure webdriver
        options = Options()
        options.page_load_strategy = "eager"
        options.add_argument('--headless')
        options.add_argument('--user-agent=%s' % USER_AGENT)
        driver = webdriver.Chrome(options=options)
        
        driver.get(self.start_url)

        # Scroll entire page
        HTMLDocumentScroller().scrollDocToEnd(driver)

        # Save html content to html file
        file_ref = f'{hashlib.sha224(b"{self.start_url}").hexdigest()}.html'
        self.save_to_file(file_ref=file_ref, driver=driver)

        # Parse the saved html
        fp = open(file_ref)
        soup = BeautifulSoup(fp, "html.parser")
        productLinks = self.parser.parse(soup=soup)

        # Close the web driver
        driver.quit()

        return productLinks