from urllib.parse import urlparse

from hyperlink import URLParseError
from base.scraper import BaseScraper
from details.parser import AmazonProductDetailParser, CourtsProductDetailParser, HNProductDetailParser, LazadaProductDetailParser, ProductDetailParser, ShopeeProductDetailParser

class ProductDetailScraper(BaseScraper):
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
        elif ('amazon.sg' in hostname) or ('amazon.com' in hostname):
            self.parser = AmazonProductDetailParser()
        else:
            print(hostname)
            raise URLParseError