import hashlib
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from hyperlink import URLParseError
from details.model import ProductDetail
from details.parser import CourtsProductDetailParser, HNProductDetailParser, LazadaProductDetailParser, ProductDetailParser, ShopeeProductDetailParser
from utilities.html_doc_scroller import HTMLDocumentScroller


class ProductDetailScraper:
    start_url: str
    parser: ProductDetailParser
    
    def __init__(self, start_url: str):
        self.start_url =  start_url
        hostname = urlparse(start_url).hostname
        if "shopee.sg" in hostname:
            self.parser = ShopeeProductDetailParser()
        elif 'lazada.sg' in hostname:
            self.parser = LazadaProductDetailParser()
        elif 'harveynorman.com.sg' in hostname:
            self.parser = HNProductDetailParser()
        elif 'courts.com.sg' in hostname:
            self.parser = CourtsProductDetailParser()
        else:
            print(hostname)
            raise URLParseError

    def save_to_file(self, file_ref: str, driver: webdriver.Chrome):
        html_file = open(file_ref, 'w')
        html_file.write(driver.page_source)
        html_file.close()

    def request(self) -> ProductDetail:
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
        productDetail = self.parser.parse(soup=soup)

        # Close the web driver
        driver.quit()

        return productDetail