import os
import base64
import requests
import datetime as dt

x_app_id= os.environ["NUTRITIONX_APP_ID"]
x_app_key = os.environ["NUTRITIONX_API_KEY"]
x_remote_user_id = "0"
headers = {
    "x-app-id": x_app_id,
    "x-app-key": x_app_key,
    "x-remote-user-id": x_remote_user_id
}

# exercises = input("Tell me which exercises you did?\n")
exercises = "run 5km and walk 2 miles"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_parameters ={
    "query": exercises,
}
today = dt.datetime.today()
today_date = today.strftime("%d/%m/%Y")
today_time = today.time().strftime("%H:%M:%S")
response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=headers)
exercise_response = response.json()["exercises"]
print(exercise_response)

sheetly_username = "35c919a6ec30d59b9847994261f581b9"
sheetly_project_name = "myWorkouts"
sheetly_sheet_name = "workouts"
sheetly_key = "alkwdjalskdjad"
sheetly_endpoint = f"https://api.sheety.co/{sheetly_username}/{sheetly_project_name}/{sheetly_sheet_name}"
headers = {
    "Authorization": "Bearer poop"
}

exercise_data = {}
for index in range(0, len(exercise_response)):
    exercise_data = {
        "workout": {
            "exercise": exercise_response[index]["name"].title(),
            "date": today_date,
            "time": today_time,
            "duration": exercise_response[index]["duration_min"],
            "calories": exercise_response[index]["nf_calories"]
            }
        }
    response = requests.post(sheetly_endpoint, json=exercise_data, headers=headers)
    print(response.text)
