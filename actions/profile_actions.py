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
            dispatcher.utter_message(text=f"To change your {user_choice}, follow these steps:\n1. Kindly check the sidebar\n2. Click settings\n3. Click \"Edit Profile\"\n4. You can now change your {user_choice}\n5. Replace the old {user_choice} with the new {user_choice} you have\n6. Click \"Save Changes\"")
        return []

class FilChangeProfile(Action):
    def name(self) -> Text:
        return "f_change_profile_steps"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_choice = tracker.get_slot("profile")

        if user_choice is None:
            dispatcher.utter_message(text="Paumanhin, ngunit hindi ko maintindihan ang impormasyong nais mong baguhin.")
        else:
            dispatcher.utter_message(text=f"Upang baguhin ang iyong {user_choice}, sundin ang mga hakbang na ito:\n1. Mangyaring tingnan ang sidebar.\n2. I-click ang \"Settings\"\n3. I-click ang \"Baguhin Ang Profile\"\n4. Maaari mo nang baguhin ang iyong {user_choice}\n5. Palitan ang lumang {user_choice} ng bagong {user_choice} na nais mo\n6. I-click ang \"Save Changes\"")
        return []
    