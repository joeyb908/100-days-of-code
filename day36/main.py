import requests
import os
from twilio.rest import Client
import datetime as dt

alphavantage_api_key = os.environ["alphavantage_api_key"]
account_sid = os.environ["twilio_account_sid"]
auth_token = os.environ["twilio_account_auth_token"]
client = Client(account_sid, auth_token)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

datetime = dt.datetime
today = datetime.now()
todays_date = today.day
yesterday = todays_date - 1
#yesterday = list[todays_date.split()]
print(todays_date)
#print(yesterday)

stock_api_endpoint = "https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alphavantage_api_key
}
# response = requests.get(url=stock_api_endpoint, params=parameters)
# response.raise_for_status()
# data = response.json()
# daily_data = data["Time Series (Daily)"]
# yesterday_open = daily_data["2022-05-02"]["1. open"]
# yesterday_close = daily_data["2022-05-02"]["4. close"]
# print(yesterday_open)


# twilio message
# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+15017122661',
#                      to='+15558675310'
#                  )
#
# print(message.sid)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

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

