from api_requests import APIRequest
from datetime_data import Date

STOCK_COMPANY = "Tesla"
STOCK_TICKER = "TSLA"

class Stocks:

    def __init__(self, api_requests: APIRequest, yesterday: Date):
        # set ticker and company to the constants
        self.ticker = STOCK_TICKER
        self.company = STOCK_COMPANY
        self.yesterday = yesterday

        # grab the json data from the api call
        self.api_request = api_requests.data

        # grab only the prior day's opening and closing stock values...
        # also calculate the delta
        self.yesterday_data = self.api_request["Time Series (Daily)"]
        self.yesterday_open = round(float(self.yesterday_data[self.yesterday]["1. open"]), 3)
        self.yesterday_close = round(float(self.yesterday_data[self.yesterday]["4. close"]), 3)
        self.yesterday_delta = float(self.calculate_percentage_change())

    def calculate_percentage_change(self):
        """Returns the percentage of change between yesterday's open and close"""
        return round(((self.yesterday_close - self.yesterday_open) / self.yesterday_open) * 100, 3)
