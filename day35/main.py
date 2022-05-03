import requests
import os
from twilio.rest import Client

# grab api key environment variable and set OpenWeatherMap endpoint
api_key = os.environ["OWM_API_KEY"]
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# set parameters for OWM
parameters = {
    "lat": 28.3,
    "lon": -82.18,
    "appid": api_key,
    "exclude": "minutely,daily,current"
}

# create connection and only pull hourly data from OWM
connection = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",
                          params=parameters)
connection.raise_for_status()
data = connection.json()
hourly_data = data["hourly"]

# for each hour in the next 12 hours, if the weather code is under 700 (likely to need umbrella)
# set bring_umbrella to true
bring_umbrella = False
for hour in range(0, 12):
    if hourly_data[hour]["weather"][0]["id"] < 700:
        print("It's going to rain!")
        bring_umbrella = True


# instructor's method
# grab a slice of the first 12 hours, then same as my method
# weather_slice = data["hourly"][:12]
# for hour in weather_slice:
#     condition_code = hour["weather"][0]["id"]
#     if condition_code < 700:
#         print("its going to rain")
#         bring_umbrella = True

# if bring umbrella is true
if bring_umbrella:
    #print(hourly_data)

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = "AC880f7790680abd16f383fb5276809e61"
    auth_token = os.environ["twilio_api_key"]
    client = Client(account_sid, auth_token)

    # send it's going to rain to my number twilio
    message = client.messages \
                    .create(
                         body="It's going to rain, bring an ☂ today!",
                         from_='+13254200769',
                         to=os.environ["cell_number"]
                     )

    print(message.status)
