import requests
from twilio.rest import Client
from auth import *

VITORIA = (42.846859, -2.671590)

URL_API_OPENWEATHER = "https://api.openweathermap.org/data/2.5/onecall"
PARAMETERS = {
        "lat": VITORIA[0],
        "lon": VITORIA[1],
        "exclude": "current,minutely,daily",
        "appid": API_KEY_OPENWEATHER,
        }

response = requests.get(url=URL_API_OPENWEATHER, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()

weather_codes_12h = [hour["weather"][0]["id"] for hour
                     in weather_data["hourly"][:12]]

if any(weather_codes_12h) < 700:
    client = Client(twilio_account_sid, twilio_auth_token)

    message = client.messages.create(
            from_="+12568260547",
            body="Bring an umbrella for the next 12 hours out of home ☂️",
            to="+34658731022")

    print("Bring an umbrella for the next 12 hours out of home ☂️")
    print(message.status)
else:
    print("No rain forecast in the next 12 hours")

#TODO:
#Replace SMS for Telegram bot, documentation: https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e
