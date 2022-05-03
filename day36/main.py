import message
import datetime_data
import api_requests
import stocks
import news

# company and ticker (refactor here to change what company you want to check)
STOCK_COMPANY = "Tesla"
STOCK_TICKER = "TSLA"

# retrieve today's date, then find what yesterday's date was
date = datetime_data.Date()
yesterday = date.yesterday

# retrieve prior day's stock data through API call
stock_request = api_requests.APIRequest("stocks")
yesterday_stock_data = stocks.Stocks(stock_request, yesterday)

# retrieve three most recent article headlines
news_request = api_requests.APIRequest("news")
news_data = news.News(news_request)

# create the message using information from the stock and news data, then send it
message = message.Message(stocks=yesterday_stock_data, news=news_data)
message.send_message()
