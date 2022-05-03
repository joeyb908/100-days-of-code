from twilio.rest import Client
from news import News
from stocks import Stocks
import os


class Message:

    # the text will have data from stock and news passed in
    def __init__(self, stocks: Stocks, news: News):

        # set stock and news data
        self.stocks = stocks
        self.news = news

        # set account credentials for twilio
        self.account_sid = os.environ['twilio_account_sid']
        self.auth_token = os.environ['twilio_account_api_key']
        self.client = Client(self.account_sid, self.auth_token)

        # set blank default headline and brief for text
        self.headline = ''
        self.brief = ''

        # if stock is positive, set positive stock delta, else set negative
        if self.stocks.yesterday_delta > 0:
            self.stock_delta = f"{self.stocks.ticker}: 🔺{self.stocks.yesterday_delta}%"
        else:
            self.stock_delta = f"{self.stocks.ticker}: 🔻{self.stocks.yesterday_delta}%"

        # set the contents of the message to be the articles from news
        self.message_contents = self.news.news_dict

    def send_message(self):
        """Send three texts, each containing the three most recent headlines"""

        # for each message in the news dictionary of articles, determine the headline and description...
        # then send the delta, headline, and description as a text to whomever
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
