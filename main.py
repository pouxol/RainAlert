from config import *
import requests
from twilio.rest import Client

weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

base_url = f"https://api.openweathermap.org/data/2.5/onecall"

weather = requests.get(base_url, params=weather_params).json()

hourly_weather = weather["hourly"]

rainy = False

for hour in hourly_weather[0:12]:
    if int(hour["weather"][0]["id"]) < 700:
        rainy = True

if rainy:
    client = Client(Account_SID, Auth_Token)
    message = client.messages \
        .create(
        body=BODY,
        from_=FROM,
        to=TO
    )
    print(message.status)
