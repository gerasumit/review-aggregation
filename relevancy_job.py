import csv
from details.scraper import ProductDetailScraper
from google.query_builder import QueryBuilder, QueryConfig
from google.search_api import OpenSearch
import time


def getUrlRelevancy(url: str) -> str:
    whitelisted_url_scheme = ["lazada.sg/products"]
    blacklisted_url_scheme = ["shopee.sg/search", "lazada.sg/tag", "shopee.sg/mall", "shopee.sg/list", "shopee.sg/collections", "amazon.sg/gp/bestsellers", "amazon.sg/stores"]
    URL_NOT_FOUND = -1


    for w_url_scheme in whitelisted_url_scheme:
        if url.find(w_url_scheme) != URL_NOT_FOUND:
            return "Whitelisted"

    for b_url_scheme in blacklisted_url_scheme:
        if url.find(b_url_scheme) != URL_NOT_FOUND:
            return "Blacklisted"

    return "Unknown"

urls_file_ref = 'test_urls.csv'
result_file_ref = 'relevancy_check.csv'

with open(urls_file_ref) as urls_csv_file, open(result_file_ref, 'w') as result_file:
    urls_reader = csv.reader(urls_csv_file)
    result_writer = csv.writer(result_file)
    result_writer.writerow(["Product Url", "Google Link", "Google Link Relevancy", "Time Taken"])
    for row in urls_reader:
        start_time = time.time()
        productUrl = row[0]
        productDetail = ProductDetailScraper(start_url=productUrl).request()
        query = QueryBuilder().build(config=QueryConfig(productDetail=productDetail))
        search_results = OpenSearch().get_search_results(q=query)
        items = search_results['items'] if 'items' in search_results else []
        googleLinks = [item['link'] for item in items]
        end_time = time.time()

        for googleLink in googleLinks:
            url_relevancy = getUrlRelevancy(googleLink)
            result_writer.writerow([productUrl, googleLink, url_relevancy, end_time-start_time])