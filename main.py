import time

import requests
from datetime import datetime
import smtplib

my_email = "zmssmzx@gmail.com"
password = "lyqi vxqn qfhq usty"
email_juan = "juanfcr11@gmail.com"

MY_LAT = -110.954929
MY_LNG = 29.158171

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# response.raise_for_status()

# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)

# print(iss_position)

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = int(datetime.now())


def iss_near():
    if MY_LAT + 5 >= iss_latitude >= MY_LAT - 5 and MY_LNG + 5 >= iss_longitude >= MY_LNG - 5:
        if sunrise >= time_now >= sunset:
            return True


while True:
    time.sleep(20)
    if iss_near():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email_juan,
                msg="Subject:La ISS esta por encima de mi casa\n\nCon +- 5 grados, pero por encima de la zona, jajaja."
                    "Va en friega esa vaina, como a 27,600 km/h (7,706.7 m/s) y a una altura de 420 km."
            )

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
