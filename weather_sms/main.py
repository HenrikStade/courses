import requests
from twilio.rest import Client

will_rain = False

# parameters = {
#     "q": "Stenlille,DK",
#     "appid": "2106a94f4be2c6a7a62c62e08d891f92"
# }
#
# response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
# response.raise_for_status()
# data = response.json()

parameters = {
    "lon": 11.5915,
    "lat": 55.5402,
    "appid": "",
    "exclude": "current,minutely,daily"
}

account_sid = ""
auth_token = ""


response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

data_12hours = weather_data["hourly"][0:11]
for hour in data_12hours:
    if int(hour["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It is going to rain. ☔",
            from_="+",
            to="+"
        )
    print(message.status)
