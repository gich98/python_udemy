import requests
import json
import datetime as dt

GENDER = "male"
WEIGHT_KG = "75"
HEIGHT_CM = 1.68
AGE = 24
NUTRITIONIX_ID = "a2ff06a1"
NUTRITIONIX_TOKEN = "327a17912e3d87c0c023f8c997bff5b1"
CONTENT_TYPE = "application/json"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/62024fe5ec2d15416a3a3bc3d1800c20/workoutsTracking/workouts"

current_day = dt.datetime.now().strftime("%Y/%m/%d")
current_hour = dt.datetime.now().strftime("%X")
user_query = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_TOKEN,
    "Content-Type": CONTENT_TYPE,
}

headers_auth = {
    "Authorization": "Bearer 327a17912e3d87c0c023f8c997bff5b1"
}

ne_body = {
    "query": user_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

ne_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=ne_body, headers=headers)
exercises = ne_response.json()["exercises"]

for exercise in exercises:
    sheety_data = {
        "workout": {
            "date": current_day,
            "time": current_hour,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_data, headers=headers_auth)
    print(sheety_response.text)

