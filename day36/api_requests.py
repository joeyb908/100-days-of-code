import requests
import os

STOCK_COMPANY = "Tesla"
STOCK_TICKER = "TSLA"


class APIRequest:

    def __init__(self, decide_api):
        self.decide_api = decide_api

        # decide what kind of API response to do: stocks or news
        # if stocks, set the ticker symbol and pass the proper parameters to alphavantage to get info
        if decide_api == "stocks":
            self.STOCK = STOCK_TICKER
            self.api_key = os.environ["alphavantage_api_key"]
            self.endpoint = "https://www.alphavantage.co/query"
            self.parameters = {
                "function": "TIME_SERIES_DAILY",
                "symbol": self.STOCK,
                "apikey": self.api_key
            }

        # if news, set the company to company and set proper parameters to newsapi to get info
        elif decide_api == "news":
            self.api_key = os.environ["newsapi_api_key"]
            self.endpoint= "https://newsapi.org/v2/top-headlines"
            self.COMPANY_NAME = STOCK_COMPANY
            self.parameters = {
                "apiKey": self.api_key,
                "q": self.COMPANY_NAME,
            }

        # make the request and store the json data for the api call
        self.data = self.receive_data()

    # receive the data
    def receive_data(self):
        """Make the api request with the chosen parameters and return the response as a json"""
        response = requests.get(url=self.endpoint, params=self.parameters)
        response.raise_for_status()
        return response.json()
