from twilio.rest import Client
from news import News
from stocks import Stocks
import os

class Message():

    def __init__(self, stocks: Stocks, news: News):
        self.stocks = stocks
        self.news = news
        self.account_sid = os.environ['twilio_account_sid']
        self.auth_token = os.environ['twilio_account_api_key']
        self.client = Client(self.account_sid, self.auth_token)

        if self.stocks.yesterday_delta > 0:
            self.stock_delta = f"{self.stocks.ticker}: 🔺{self.stocks.yesterday_delta}%"
        else:
            self.stock_delta = f"{self.stocks.ticker}: 🔻{self.stocks.yesterday_delta}%"

        self.message_contents = self.news.news_dict

    def send_message(self):
        for message in range(0, 3):
            self.headline = self.message_contents[message]["title"]
            self.brief = self.message_contents[message]["description"]
            message = self.client.messages \
                            .create(
                                 body=f"{self.stock_delta}\n"
                                      f"Headline: {self.headline}\n"
                                      f"Brief: {self.brief}\n",
                                 from_='+13254200769',
                                 to='+15613120537'
                             )

        print(message.status)
