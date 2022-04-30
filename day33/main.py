import smtplib
import time

import requests
from datetime import datetime

# set my email and pass
MY_EMAIL = "tet.tst@email.com"
MY_PASS = "password"

# set my long and lat
MY_LAT = 28.665409
MY_LONG = -81.210594
my_position = (MY_LONG, MY_LAT)

# get ISS position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])
iss_position = (longitude, latitude)

# get sunrise and sunset times in UTC for my long and lat
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json?lat", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.now()

# split sunrise and sunset times to only grab the hours out of 24
sunrise = (int(sunrise.split("T")[1].split(":")[0]) - 4) % 24
sunset = (int(sunset.split("T")[1].split(":")[0]) - 4) % 24

# can be made to run every 60 seconds to allow for some power saving...
# while True:
#     time.sleep(60)
# if iss is overhead
if -5 <= MY_LAT - iss_position[1] <= 5 and -5 <= MY_LONG - iss_position[0] <= 5:
    # and it's dark outside
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        # send an email to me saying it's above
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="test@email.com",
                msg=f"Subject:ISS Notifier\n\n"
                    f"The ISS is near overhead and you should be able to see it!"
            )
