import requests
import os

class API_Request():

    def __init__(self, decide_api):
        self.decide_api = decide_api

        # decide what kind of API response to do
        # stocks, news, or twilio
        if decide_api == "stocks":
            self.STOCK = "TSLA"
            self.api_key = os.environ["alphavantage_api_key"]
            self.endpoint = "https://www.alphavantage.co/query"
            self.parameters = {
                "function": "TIME_SERIES_DAILY",
                "symbol": self.STOCK,
                "apikey": self.api_key
            }
        elif decide_api == "news":
            self.api_key = os.environ["newsapi_api_key"]
            self.endpoint= "https://newsapi.org/v2/top-headlines"
            self.COMPANY_NAME = "Tesla"
            self.parameters = {
                "apiKey": self.api_key,
                "q": self.COMPANY_NAME,
            }
        elif decide_api == "message":
            self.sid = os.environ["twilio_account_sid"]
            self.api_key = os.environ["twilio_account_api_key"]
            self.endpoint = ""


    def receive_data(self):
        response = requests.get(url=self.endpoint, params=self.parameters)
        response.raise_for_status()
        return response.json()