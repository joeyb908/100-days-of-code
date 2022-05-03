import message
import datetime_data
import api_requests
import stocks
import news

# retrieve today's date, then find what yesterday's date was
date = datetime_data.Date()
yesterday = date.yesterday

# retrieve prior day's stock data through API call
stock_request = api_requests.API_Request("stocks").receive_data()
yesterday_stock_data = stocks.Stocks(stock_request, yesterday)

# retrieve three most recent article headlines
news_request = api_requests.API_Request("news").receive_data()
news_data = news.News(news_request)

# create the message using information from the stock and news data, then send it
message = message.Message(stocks=yesterday_stock_data, news=news_data)
message.send_message()

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""