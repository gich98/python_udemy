import requests
import datetime as dt

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
OWM_API_KEY = "OWM_API_KEY"
current_hour = dt.datetime.now().hour
parameters = {
    "lat": 51,
    "lon": 0,
    "exclude": "current,minutely,daily",
    "appid": OWM_API_KEY,
}

if current_hour != 7:
    response = requests.get(url=OWM_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()
    weather_12_hours = data["hourly"][:12]
    rainy_hour = [weather for weather in weather_12_hours if weather["weather"][0]["id"] < 700]
    if len(rainy_hour) != 0:
        print("Take the umbrella! In the next 12 hours it will rain/snow.")
    else:
        print("Today is really a good day! It won't rain!")
else:
    print(f"It's currently {current_hour}")
