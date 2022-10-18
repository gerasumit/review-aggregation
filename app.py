from flask import Flask
from flask import request
from details.scraper import ProductDetailScraper
from google.query_builder import QueryBuilder, QueryConfig
from product_links.scraper import ProductLinkScraper
import logging

app = Flask(__name__)

@app.route('/reviews/', methods=['POST'])
def reviews():
    productUrl = request.form['product_url']
    productDetail = ProductDetailScraper(start_url=productUrl).request()
    query = QueryBuilder().build(config=QueryConfig(productDetail=productDetail))
    productLinks = ProductLinkScraper(start_url="https://www.google.com/search?q=" + query).request()
    response = {
        'product_detail': {
            'description': productDetail.description,
            'model': productDetail.model
        },
        'google_links': [link.link for link in productLinks]
    }
    return response, 200, {'Content-Type':'application/json'}

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500