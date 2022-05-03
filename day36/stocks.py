from api_requests import API_Request
from datetime_data import Date

class Stocks():

    def __init__(self, api_requests: API_Request, yesterday: Date):
        self.ticker = "TSLA"
        self.company = "Tesla"
        self.api_request = api_requests
        self.daily_data = self.api_request["Time Series (Daily)"]
        self.yesterday_open = round(float(self.daily_data[yesterday]["1. open"]), 3)
        self.yesterday_close = round(float(self.daily_data[yesterday]["4. close"]), 3)
        self.yesterday_delta = float(self.calculate_percentage_change())

    def calculate_percentage_change(self):
        return round(((self.yesterday_close - self.yesterday_open) / self.yesterday_open) * 100, 3)