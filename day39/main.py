import os
import requests
import datetime as dt
from twilio.rest import Client

# grab the date for one/two weeks, and six months ahead
one_week_ahead = (dt.datetime.today() + dt.timedelta(days=7)).strftime("%d/%m/%Y")
two_weeks_ahead = (dt.datetime.today() + dt.timedelta(days=14)).strftime("%d/%m/%Y")
six_months_ahead = (dt.datetime.today() + dt.timedelta(days=182)).strftime("%d/%m/%Y")

# set the information needed to interact with the tequila-kiwi API for flight pricing information
kiwi_affillID = "joeyb908learningapis"
kiwi_api_key = os.environ["kiwi_api_key"]
kiwi_endpoint = "https://tequila-api.kiwi.com/v2/search"
header = {
    "apikey": kiwi_api_key
}

# set up destinations I want to visit, as well as two accompanying dictionaries
destination_cost = {}
destinations_dict = {}
destinations = ["FRA", "CDG", "JFK", "LGA", "LAX", "SFO", "JAC", "EWR"]
for destination in destinations:
    kiwi_parameters = {
        "fly_from": "MCO",
        "fly_to": destination,
        "date_from": one_week_ahead,
        "date_to": six_months_ahead,
        "nights_in_dst_to": 10,
        "nights_in_dst_from": 10,
        "flight_type": "round",
        "one_for_city": 1,
        "adults": 2,
        "curr": "USD",
        "conn_on_diff_airport": 0
    }

    # if the API call fails, retries
    success = False
    while not success:
        try:
            response = requests.get(url=kiwi_endpoint, params=kiwi_parameters, headers=header)
            flight_data = response.json()["data"][0]
        except IndexError:
            pass
        else:
            success = True

    # sets price, city, and airport code
    price = flight_data["price"]
    city = flight_data["cityTo"]
    code = flight_data["flyTo"]

    # places city in the destination dict if it's not there, otherwise it compares the price, if price is lower
    # then it will replace (useful for NYC b/c it has 3 airports), otherwise it passes
    if city not in destinations_dict:
        destinations_dict.update({city: {"price": price, "flyTo": code}})
    elif price < destinations_dict[city]["price"]:
        destinations_dict.update({city: {"price": price, "flyTo": code}})
    else:
        pass
    print("Please hold... pulling data... \n")

print("Data gathered... manipulating the doc now")

# gets sheety info to make the api call
sheety_user = os.environ["sheety_user"]
sheety_project = "cheapFlightFinder"
sheety_sheet = "sheet1"
sheety_endpoint_get = f"https://api.sheety.co/{sheety_user}/{sheety_project}/{sheety_sheet}"
row_num = 2
sheety_endpoint_put = f"https://api.sheety.co/{sheety_user}/{sheety_project}/{sheety_sheet}/{row_num}"

# creates the dictionary that will be used to update the Google Sheets doc
sheety_update = {}
for destination in destinations_dict:
    sheety_update = {"sheet1":
        {
            "city": destination,
            "airportCode": destinations_dict[destination]["flyTo"],
            "lowestPrice": destinations_dict[destination]["price"]
        }
    }

    # updates the data in the Google Sheets doc, then updates the endpoint to work for the new row
    update_data = requests.put(url=sheety_endpoint_put, json=sheety_update)
    row_num += 1
    sheety_endpoint_put = f"https://api.sheety.co/{sheety_user}/{sheety_project}/{sheety_sheet}/{row_num}"

# sets and creates the variables for the SMS to be sent
account_sid = os.environ["twilio_account_sid"]
twilio_auth_token = os.environ["twilio_auth_token"]
client = Client(account_sid, twilio_auth_token)

sheet_data = requests.get(url=sheety_endpoint_get).json()["sheet1"]
# compares the updated price to the threshold price and sends a text with the city and price differential between the
# target
for destination in sheet_data:
    difference = destination["lowestPrice"] - destination["targetPrice"]
    if difference < 0:
        print("it works")
        message = client.messages \
            .create(
                body=f"Quick! Go book a flight to {destination['city']}, "
                     f"the price is ${abs(difference)} below your target!",
                from_='+13254200769',
                to='+15613120537'
            )
        print(message.status)
