import requests

class OpenSearch:
    def get_search_results(self, q: str):
        params = {}
        params["key"] = "<API_KEY>"
        params["cx"] = "03cc508b073224774"
        params["q"] = q
        
        response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
        return response.json()