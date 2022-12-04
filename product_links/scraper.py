
from typing import List
from base.scraper import BaseScraper
from product_links.parser import ProductLinkParser

class ProductLinkScraper(BaseScraper):
    start_url: str
    parser: ProductLinkParser
    
    def __init__(self, start_url: str):
        self.start_url =  start_url
        self.parser = ProductLinkParser()