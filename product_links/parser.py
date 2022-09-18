from typing import List
from product_links.model import ProductLink
from bs4 import BeautifulSoup

class ProductLinkParser:
    def parse(self, soup: BeautifulSoup) -> List[ProductLink]:
        products = soup.find_all(attrs={"class":"yuRUbf"})
        product_links = [ProductLink(link=div_soup.a["href"]) for div_soup in products]
        return product_links