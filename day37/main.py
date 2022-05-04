import requests
import os
from datetime import datetime as dt

# set username, token, API endpoint, formatted date, graph ID, and header
USERNAME = "joeyb908"
TOKEN = os.environ["PIXELA_TOKEN"]
pixela_endpoint = "https://pixe.la/v1/users"
today = dt.now()
formatted_date = today.strftime("%Y%m%d")
graph_id = "graph1"
headers = {
    "X-USER-TOKEN": TOKEN
}


def create_new_user():
    """Create a new user for the website"""
    # user parameters to actually create a new user
    user_parameters = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    # create pixela user
    response = requests.post(url=pixela_endpoint, json=user_parameters)
    print(response.text)


def create_graph():
    """Create a graph to start tracking data"""

    # graph endpoint & parameters
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_config = {
        "id": "graph1",
        "name": "Programming Graph",
        "unit": "min",
        "type": "int",
        "color": "ajisai"
    }

    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


def post_min():
    """Post a new entry for today"""
    # endpoint and parameters to do so
    post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
    post_pixel_parameters = {
        "date": formatted_date,
        "quantity": input("How many minutes did you program today? "),
    }

    response = requests.post(url=post_pixel_endpoint, json=post_pixel_parameters, headers=headers)
    print(response.text)


def update_min():
    """Update an entry (can be past entry)"""
    # endpoint and parameters needed to do so
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{formatted_date}"
    update_parameters = {
        "quantity": "78",
    }
    response = requests.put(url=update_endpoint, json=update_parameters, headers=headers)
    print(response.text)


post_min()
