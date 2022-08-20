from details.model import ProductDetail
from details.scraper import ProductDetailScraper
from reviews.model import ProductReview
from reviews.scraper import ReviewsScraper
from typing import List

from utilities.performance_util import CodeTimer

def printReview(reviews=List[ProductReview]):
    [print(review.author, review.review, review.reviewed_at, review.meta, "\n") for review in reviews]

def printProductDetail(productDetail=ProductDetail):
    [print(productDetail.description, productDetail.model)]
    
SHOPEE_URL = "https://shopee.sg/SPICY-MAMA-Extra-Spicy-Crispy-Anchovy-and-Shrimp-130-grams-i.3343488.9959517533?sp_atk=78942143-1f4f-4c0a-84c3-a4e68ea2af7a&xptdk=78942143-1f4f-4c0a-84c3-a4e68ea2af7a"
LAZADA_URL = "https://www.lazada.sg/products/fotile-multifunctional-4-in-1-countertop-oven-steaming-baking-air-frying-dehydrating-humanized-design-hyzk26-e1-i1983285397-s10725255226.html"
HN_URL = "https://www.harveynorman.com.sg/computing/computers-en/laptops-en/lenovo-yoga-7-core-i7-16gb-1tb-windows-11-14-inch-convertible-laptop-storm-grey-14ial7-82qe002rsb.html"

urls = [
    SHOPEE_URL,
    LAZADA_URL,
    HN_URL
]

# Print reviews
[printReview(ReviewsScraper(start_url=url).request()) for url in urls]

# Print product detail
for url in urls:
    printProductDetail(ProductDetailScraper(start_url=url).request())