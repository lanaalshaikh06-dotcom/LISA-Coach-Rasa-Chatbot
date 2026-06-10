# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# -------------------------------
# الأكشن الافتراضي (لا تلمسيه)
# -------------------------------

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


# -------------------------------
# الأكشن الجديد: قراءة بيانات من الموقع
# -------------------------------

import requests
from bs4 import BeautifulSoup
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionReadFromMuscleAndStrength(Action):

    def name(self):
        return "action_read_from_muscleandstrength"

    def run(self, dispatcher, tracker, domain):

        url = "https://www.muscleandstrength.com/workouts"  # صفحة التمارين

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            # استخراج أول عنوان تمرين كمثال
            workout_title = soup.find("h2").get_text(strip=True)

            dispatcher.utter_message(
                text=f"Here is something I found on Muscle & Strength:\n\n{workout_title}\n\nSource: {url}"
            )

        except Exception as e:
            dispatcher.utter_message(text="Sorry, I couldn't fetch data from the website.")

        return []