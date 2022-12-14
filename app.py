from flask import Flask
from flask import request
from details.scraper import ProductDetailScraper
from google.query_builder import QueryBuilder, QueryConfig
from product_links.scraper import ProductLinkScraper
import logging
from google.search_api import OpenSearch

app = Flask(__name__)

@app.route('/reviews/', methods=['POST'])
def reviews():
    productUrl = request.form['product_url']
    productDetail = ProductDetailScraper(start_url=productUrl).request()
    query = QueryBuilder().build(config=QueryConfig(productDetail=productDetail))
    search_results = OpenSearch().get_search_results(q=query)
    productUrls = [item['link'] for item in search_results['items']] if search_results['items'] is not None else []
    # productLinksUrl = "https://www.google.com/search?q=" + query
    # productLinks = ProductLinkScraper(start_url=productLinksUrl).request()
    # productUrls = [link.link for link in productLinks]
    response = {
        'product_detail': {
            'description': productDetail.description,
            'model': productDetail.model
        },
        'product_urls': productUrls
    }
    return response, 200, {'Content-Type':'application/json'}

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

if __name__ == "__main__":
    app.run(debug=True)