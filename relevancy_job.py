import csv
from details.scraper import ProductDetailScraper
from google.query_builder import QueryBuilder, QueryConfig
from google.search_api import OpenSearch
import time
from enum import Enum
import sys, time
import re

class URLRelevancy(Enum):
    WHITELISTED = 1
    BLACKLISTED = 2
    REMOVED = 3
    UKNOWN = 4

def getUrlRelevancy(url: str) -> URLRelevancy:
    whitelisted_url_scheme = [
        ".+lazada.sg/products.+"
    ]
    blacklisted_url_scheme = [
        ".+shopee.sg/search.+",
        ".+shopee.sg/m/.+", 
        ".+lazada.sg/tag.+", 
        ".+shopee.sg/mall.+", 
        ".+shopee.sg/list.+", 
        ".+shopee.sg/collections.+", 
        ".+amazon.(?:sg|com)/gp/bestsellers.+", 
        ".+amazon.(?:sg|com)/stores.+", 
        ".+amazon.(?:sg|com)/vdp.+", 
        ".+amazon.(?:sg|com)/gp/.+", 
        ".+amazon.(?:sg|com).+/s?.+",
        ".+amazon.(?:sg|com)/stores.+",
        ".+amazon.(?:sg|com).+b?ie.+"
    ]


    for w_url_scheme in whitelisted_url_scheme:
        if re.fullmatch(w_url_scheme, url) is not None:
            return URLRelevancy.WHITELISTED

    for b_url_scheme in blacklisted_url_scheme:
        if re.fullmatch(b_url_scheme, url) is not None:
            return URLRelevancy.BLACKLISTED


    return URLRelevancy.UKNOWN

urls_file_ref = 'test_urls.csv'
result_file_ref = 'relevancy_check.csv'

with open(urls_file_ref) as urls_csv_file, open(result_file_ref, 'w') as result_file:
    urls_reader = csv.reader(urls_csv_file)
    result_writer = csv.writer(result_file)
    result_writer.writerow(["Product Url", "Google Link", "Query", "Google Link Relevancy", "Time Taken"])
    
    for row in urls_reader:
        # Processing item ...
        print(f"Processing item {urls_reader.line_num}...", end='\r')

        start_time = time.time()
        productUrl = row[0]
        productDetail, isRemoved = ProductDetailScraper(start_url=productUrl).request()
        query = QueryBuilder().build(config=QueryConfig(productDetail=productDetail))
        search_results = OpenSearch().get_search_results(q=query)
        items = search_results['items'] if 'items' in search_results else []
        googleLinks = [item['link'] for item in items]
        end_time = time.time()

        for googleLink in googleLinks:
            url_relevancy = getUrlRelevancy(googleLink)
            if isRemoved:
                url_relevancy = URLRelevancy.REMOVED
            result_writer.writerow([productUrl, googleLink, query, url_relevancy, end_time-start_time])