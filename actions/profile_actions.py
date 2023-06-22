# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ChangeProfile(Action):
    def name(self) -> Text:
        return "change_profile_steps"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_choice = tracker.get_slot("profile")

        if user_choice is None:
            dispatcher.utter_message(text="I'm sorry, I didn't understand the information you want to change.")
        else:
            dispatcher.utter_message(text=f"To change your {user_choice}, follow these steps:\n1. Click the side bar menu\n2. Click settings\n3. Click \"Edit Profile\"\n4. You can now change your {user_choice}\n5. Replace the old {user_choice} with the new {user_choice} you have\n6. Click \"Save Changes\"")
        return []
    