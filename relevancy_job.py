import csv
from details.scraper import ProductDetailScraper

from google.query_builder import QueryBuilder, QueryConfig
from google.search_api import OpenSearch



# Generate results

urls_file_ref = 'test_urls.csv'
result_file_ref = 'relevancy_check.csv'
with open(urls_file_ref) as urls_csv_file, open(result_file_ref, 'w') as result_file:
    urls_reader = csv.reader(urls_csv_file)
    result_writer = csv.writer(result_file)
    for row in urls_reader:
        productUrl = row[0]
        productDetail = ProductDetailScraper(start_url=productUrl).request()
        query = QueryBuilder().build(config=QueryConfig(productDetail=productDetail))
        search_results = OpenSearch().get_search_results(q=query)
        productUrls = [item['link'] for item in search_results['items']] if search_results['items'] is not None else []
        result_row = [productUrl, '|'.join(productUrls)]
        result_writer.writerow(result_row)

# Put them in tests