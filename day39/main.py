import requests
import datetime as dt

one_week_ahead = (dt.datetime.today() + dt.timedelta(days=7)).strftime("%d/%m/%Y")
two_weeks_ahead = (dt.datetime.today() + dt.timedelta(days=14)).strftime("%d/%m/%Y")
six_months_ahead = (dt.datetime.today() + dt.timedelta(days=182)).strftime("%d/%m/%Y")

kiwi_affillID = "joeyb908learningapis"
kiwi_api_key = "y6HNIitljuhUViC6rq4QXvJpWsVrluOf"
kiwi_endpoint = "https://tequila-api.kiwi.com/v2/search"
header = {
    "apikey": kiwi_api_key
}

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

    response = requests.get(url=kiwi_endpoint, params=kiwi_parameters, headers=header)
    success = False
    while not success:
        try:
            flight_data = response.json()["data"][0]
        except IndexError:
            pass
        else:
            success = True
    price = flight_data["price"]
    city = flight_data["cityTo"]
    code = flight_data["flyTo"]
    if city not in destinations_dict:
        destinations_dict.update({city: {"price": price, "flyTo": code}})
    elif price < destinations_dict[city]["price"]:
        destinations_dict.update({city: {"price": price, "flyTo": code}})
    else:
        pass

#print(destinations_dict)

sheety_user = "35c919a6ec30d59b9847994261f581b9"
sheety_project = "cheapFlightFinder"
sheety_sheet = "sheet1"
row_num = 2
#sheety_endpoint = f"https://api.sheety.co/{sheety_user}/{sheety_project}/{sheety_sheet}"
sheety_endpoint_put = f"https://api.sheety.co/{sheety_user}/{sheety_project}/{sheety_sheet}/{row_num}"
# sheet_data = requests.get(url=sheety_endpoint)
# sheet_data = {
#     "sheet1": [
#         {
#             "city": "Frankfurt",
#             "airportCode": "FRA",
#             "targetPrice": 800,
#             "lowestPrice": 1532,
#             "id": 2
#         },
#         {
#             "city": "Paris",
#             "airportCode": "CDG",
#             "targetPrice": 800,
#             "lowestPrice": 785,
#             "id": 3
#         },
#         {
#             "city": "Jackson Hole",
#             "airportCode": "JAC",
#             "targetPrice": 200,
#             "lowestPrice": 753,
#             "id": 4
#         },
#         {
#             "city": "New York",
#             "airportCode": "LGA",
#             "targetPrice": 200,
#             "lowestPrice": 153,
#             "id": 5
#         },
#         {
#             "city": "San Francisco",
#             "airportCode": "SFO",
#             "targetPrice": 200,
#             "lowestPrice": 432,
#             "id": 6
#         },
#         {
#             "city": "Los Angeles",
#             "airportCode": "LAX",
#             "targetPrice": 200,
#             "lowestPrice": 354,
#             "id": 7
#         }
#     ]
# }

# [print(
#     f"Quick! Go buy a ticket to {destination['city']}, "
#     f"tickets are lower than your ${destination['targetPrice']} price point.")
#  for destination in sheet_data["sheet1"]
#  if destination["lowestPrice"] < destination["targetPrice"]]
sheety_update = {}
for destination in destinations_dict:
    sheety_update = {"sheet1":
            {
                "city": destination,
                "airportCode": destinations_dict[destination]["flyTo"],
                "lowestPrice": destinations_dict[destination]["price"]
            }
    }
    print(sheety_update)
    update_data = requests.put(url=sheety_endpoint_put, json=sheety_update)
    print(update_data.text)
    print(sheety_endpoint_put)
    row_num += 1
    sheety_endpoint_put = f"https://api.sheety.co/{sheety_user}/{sheety_project}/{sheety_sheet}/{row_num}"



