from api_requests import APIRequest


class News:

    def __init__(self, api_requests: APIRequest):
        # grab the news data and only ull the first 3 articles
        self.news_data = api_requests.data
        self.articles = self.news_data["articles"][:3]

        # create a list with dictionary within that holds the article title and description
        self.news_dict = [{
            "title": article["title"],
            "description": article["description"]
        } for article in self.articles]
