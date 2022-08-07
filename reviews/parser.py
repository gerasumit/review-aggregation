from typing import List, Protocol

from bs4 import BeautifulSoup
from reviews.model import ProductReview


class ReviewsParser(Protocol):
    def parse(self) -> List[ProductReview]:
        raise NotImplemented

class ShopeeReviewsParser(ReviewsParser):
    def parse(self, file_ref: str) -> List[ProductReview]:
        reviews = []

        with open(file_ref) as fp:
            soup = BeautifulSoup(fp, "html.parser")

            divs = soup.find_all(attrs={"class":"shopee-product-rating"})
            for div in divs:
                author = div.find(attrs={"class": "shopee-product-rating__author-name"}).string
                purchase_detail = div.find(attrs={"class": "shopee-product-rating__time"}).string
                variant = ''
                review_date = ''
                review_div = div.find(attrs={"class": "Em3Qhp"})
                review = review_div.string if review_div is not None else ""
                reviews.append(ProductReview(author=author, review=review, reviewed_at=review_date, meta=purchase_detail))
        
        return reviews

class LazadaReviewsParser(ReviewsParser):
    def parse(self, file_ref: str) -> List[ProductReview]:
        reviews = []

        with open(file_ref) as fp:
            soup = BeautifulSoup(fp, "html.parser")

            reviews_div = soup.find(attrs={"class":"mod-reviews"})
            review_items = reviews_div.find_all(attrs={"class":"item"})
            for review_item in review_items:
                author = review_item.find(attrs={"class": "middle"}).find_all('span')[0].string.replace("by ", "")
                review = review_item.find(attrs={"class": "item-content"}).find(attrs={"class": "content"}).string
                reviewed_at = review_item.find(attrs={"class": "top"}).find(attrs={"class": "title right"}).string
                meta = review_item.find(attrs={"class":"skuInfo"}).string
                reviews.append(ProductReview(author=author, review=review, reviewed_at=reviewed_at, meta=meta))
        
        return reviews