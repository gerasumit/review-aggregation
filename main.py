from reviews.model import ProductReview
from reviews.scraper import ReviewsScraper
from typing import List

def printReview(reviews=List[ProductReview]):
    [print(review.author, review.review, review.reviewed_at, review.meta, "\n") for review in reviews]

SHOPEE_URL = "https://shopee.sg/SPICY-MAMA-Extra-Spicy-Crispy-Anchovy-and-Shrimp-130-grams-i.3343488.9959517533?sp_atk=78942143-1f4f-4c0a-84c3-a4e68ea2af7a&xptdk=78942143-1f4f-4c0a-84c3-a4e68ea2af7a"
LAZADA_URL = "https://www.lazada.sg/products/lulufurnituresgdesigner-dining-chair-with-comfort-arm-rest-back-rest-price-including-delivery-i1239262907-s5066923000.html?spm=a2o42.home.flashSale.4.654346b52ETREX&search=1&mp=1&c=fs&clickTrackInfo=rs%3A0.1067863404750824%3Bfs_item_discount_price%3A19.90%3Bitem_id%3A1239262907%3Bmt%3Ahot%3Bfs_utdid%3A-1%3Bfs_item_sold_cnt%3A12%3Babid%3A287818%3Bfs_item_price%3A38.90%3Bpvid%3Adb52d104-e526-495e-80c6-dbc11e78d086%3Bfs_min_price_l30d%3A0%3Bdata_type%3Aflashsale%3Bfs_pvid%3Adb52d104-e526-495e-80c6-dbc11e78d086%3Btime%3A1658672170%3Bfs_biz_type%3Afs%3Bscm%3A1007.17760.287818.%3Bchannel_id%3A0000%3Bfs_item_discount%3A49%25%3Bcampaign_id%3A182337&scm=1007.17760.287818.0"

urls = [
    SHOPEE_URL,
    LAZADA_URL
]

[printReview(ReviewsScraper(start_url=url).request()) for url in urls]