import csv
from details.scraper import ProductDetailScraper
from google.query_builder import QueryBuilder, QueryConfig
from google.search_api import OpenSearch
import time

urls_file_ref = 'test_urls.csv'
result_file_ref = 'relevancy_check.csv'
with open(urls_file_ref) as urls_csv_file, open(result_file_ref, 'w') as result_file:
    urls_reader = csv.reader(urls_csv_file)
    result_writer = csv.writer(result_file)
    for row in urls_reader:
        start_time = time.time()
        productUrl = row[0]
        productDetail = ProductDetailScraper(start_url=productUrl).request()
        query = QueryBuilder().build(config=QueryConfig(productDetail=productDetail))
        search_results = OpenSearch().get_search_results(q=query)
        googleLinks = [item['link'] for item in search_results['items']] if search_results['items'] is not None else []
        end_time = time.time()
        for googleLink in googleLinks:
             result_writer.writerow([productUrl, googleLink, end_time-start_time])