import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "vg.checkrain@gmail.com"
MY_PWD = "1234567890asD."
MY_LAT = -50.117142
MY_LONG = -138.871872
ERROR_MARGIN = 5


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if ((iss_latitude - ERROR_MARGIN) <= MY_LAT <= (iss_latitude + ERROR_MARGIN) and
            (iss_longitude - ERROR_MARGIN) <= MY_LONG <= (iss_longitude + ERROR_MARGIN)):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = datetime.now().hour
    if not (sunrise <= current_hour <= sunset):
        return True


while True:
    if is_overhead() and is_night():
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PWD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject:ISS\n\nLook up in the sky, the ISS is above you!")
    time.sleep(60)
