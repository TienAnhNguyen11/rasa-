
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests, json

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather_answering"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import requests, json

        api_key = "920c80b837ed9e7573c083dc531361fa"

        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        city_name = tracker.slots.get("city_name")

        day = tracker.slots.get("day")

        complete_url = base_url + "appid=" + api_key + "&q=" + str(city_name)

        response = requests.get(complete_url)

        x = response.json()

        if x["cod"] != "404":

            y = x["main"]

            current_temperature = round(y["temp"] - 272.15)

            current_humidity = y["humidity"]

            z = x["weather"]

            weather_description = z[0]["description"]

            dispatcher.utter_message("Dạ, thời tiết tại {} {}\nNhiệt độ: {}\n Độ ẩm: {}\n, {}".format(city_name, day, current_temperature, current_humidity, weather_description))
        else:
            print(" City Not Found ")

        return []
