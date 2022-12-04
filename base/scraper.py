from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from utilities.html_doc_scroller import HTMLDocumentScroller
import hashlib

class BaseScraper:
    start_url: str

    def __init__(self, start_url: str):
        self.start_url = start_url

    def save_to_file(self, file_ref: str, driver: webdriver.Firefox):
        html_file = open(file_ref, 'w')
        html_file.write(driver.page_source)
        html_file.close()

    def request(self):
        # Configure webdriver
        options = Options()
        options.page_load_strategy = "eager"
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.get(self.start_url)

        # Scroll entire page
        HTMLDocumentScroller().scrollDocToEnd(driver)

         # Save html content to html file
        file_ref = f'{hashlib.sha224(b"{self.start_url}").hexdigest()}.html'
        self.save_to_file(file_ref=file_ref, driver=driver)

        # Parse the saved html
        fp = open(file_ref)
        soup = BeautifulSoup(fp, "html.parser")
        response = self.parser.parse(soup=soup)

        # Close the web driver
        driver.quit()

        return response