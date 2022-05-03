from api_requests import API_Request
from stocks import Stocks

class News():

    def __init__(self, api_requests: API_Request):
        self.news_data = api_requests
        self.articles = self.news_data["articles"][:3]
        self.titles_descriptions = []
        self.news_dict = [{
            "title": article["title"],
            "description": article["description"]
        } for article in self.articles]
