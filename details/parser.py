from itertools import product
from turtle import title
from bs4 import BeautifulSoup

from details.model import ProductDetail

class ProductDetailParser:
    def parse(self, soup: BeautifulSoup) -> ProductDetail:
        raise NotImplementedError

class LazadaProductDetailParser(ProductDetailParser):
    def parse(self, soup: BeautifulSoup) -> ProductDetail:
        title_elem = soup.find(attrs={"class":"pdp-mod-product-badge-title"})
        productDetail = ProductDetail(description=title_elem.string if title_elem is not None else "")
        return productDetail

class ShopeeProductDetailParser(ProductDetailParser):
    def parse(self, soup: BeautifulSoup) -> ProductDetail:
        title_div = soup.find(attrs={"class":"_2rQP1z"})
        productDetail = ProductDetail(description=title_div.span.string if title_div is not None else "")
        return productDetail

class HNProductDetailParser(ProductDetailParser):
    def parse(self, soup: BeautifulSoup):
        title_h1 = soup.find(attrs={"class": "product-title"})
        productDetail = ProductDetail(description=title_h1.string if title_h1 is not None else "") 
        return productDetail

class CourtsProductDetailParser(ProductDetailParser):
    def parse(self, soup: BeautifulSoup) -> ProductDetail:
        title_h1 = soup.find(attrs={"class": "page-title"})
        productDetail = ProductDetail(description=title_h1.string if title_h1 is not None else "")
        return productDetail