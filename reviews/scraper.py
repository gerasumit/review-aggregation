from urllib.parse import urlparse
from hyperlink import URLParseError
from base.scraper import BaseScraper
from reviews.parser import LazadaReviewsParser, ReviewsParser, ShopeeReviewsParser

class ReviewsScraper(BaseScraper):
    start_url: str
    parser: ReviewsParser
    
    def __init__(self, start_url: str):
        self.start_url =  start_url
        hostname = urlparse(start_url).hostname
        if "shopee.sg" in hostname:
            self.parser = ShopeeReviewsParser()
        elif 'lazada.sg' in hostname:
            self.parser = LazadaReviewsParser()
        else:
            print(hostname)
            raise URLParseError