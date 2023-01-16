from typing import List
from details.model import ProductDetail

class QueryConfig: 
    supportedWebsites: List[str]
    productDetail: ProductDetail

    def __init__(self, productDetail: ProductDetail):
        self.supportedWebsites = ["shopee.sg", "lazada.sg", "amazon.sg", "amazon.com"]
        self.productDetail = productDetail

class QueryBuilder:
    def build(self, config: QueryConfig) -> str:
        query = ""
        
        if config.productDetail.model is not None and config.productDetail.model != "":
            query += "\"" + config.productDetail.model + "\"" + " "

        if config.productDetail.description is not None and config.productDetail.description != "":
            query += config.productDetail.description

        query += " AND " + " OR ".join(["site:" + site for site in config.supportedWebsites])
        
        return query