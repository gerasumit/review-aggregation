import requests

class OpenSearch:
    def get_search_results(self, q: str):
        params = {}
        params["q"] = q
        
        response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
        return response.json()