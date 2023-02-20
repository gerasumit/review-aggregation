from bs4 import BeautifulSoup
from details.model import ProductDetail
from typing import Optional, Tuple

class ProductDetailParser:
    def parse(self, soup: BeautifulSoup) -> Tuple[Optional[ProductDetail], Optional[bool]]:
        raise NotImplementedError

class LazadaProductDetailParser(ProductDetailParser):
    def parse(self, soup: BeautifulSoup) -> Tuple[Optional[ProductDetail], Optional[bool]]:
        title_elem = soup.find(attrs={"class":"pdp-mod-product-badge-title"})
        productDetail = ProductDetail(description=title_elem.string if title_elem is not None else "")
        return productDetail, None

class ShopeeProductDetailParser(ProductDetailParser):
    def parse(self, soup: BeautifulSoup) -> Tuple[Optional[ProductDetail], Optional[bool]]:
        title_div = soup.find(attrs={"class":"_44qnta"})
        productDetail = ProductDetail(description=title_div.span.string if title_div is not None else "")
        return productDetail, None

class HNProductDetailParser(ProductDetailParser):
    def parse(self, soup: BeautifulSoup) -> Tuple[Optional[ProductDetail], Optional[bool]]:
        title_h1 = soup.find(attrs={"class": "product-title"})
        productDetail = ProductDetail(description=title_h1.string if title_h1 is not None else "") 
        return productDetail, None

class CourtsProductDetailParser(ProductDetailParser):
    def parse(self, soup: BeautifulSoup) -> Tuple[Optional[ProductDetail], Optional[bool]]:
        title_h1 = soup.find(attrs={"class": "page-title"})
        productDetail = ProductDetail(description=title_h1.string if title_h1 is not None else "")
        return productDetail, None

class AmazonProductDetailParser(ProductDetailParser):
    def parse(self, soup: BeautifulSoup) -> Tuple[Optional[ProductDetail], Optional[bool]]:
        title_item = soup.find(attrs={"id": "productTitle"})
        model_tr = soup.find(attrs={"class": "po-model_name"})
        model_name = model_tr.find(attrs={"class":"po-break-word"}) if model_tr is not None else None
        productDetail = ProductDetail(description=title_item.string if title_item is not None else "", model=model_name.string if model_name is not None else "")
        return productDetail, None