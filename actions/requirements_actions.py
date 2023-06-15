# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class DocumentRequirements(Action):
    def name(self) -> Text:
        return "requirements_needed"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_choice = tracker.get_slot("document")

        if user_choice is None:
            dispatcher.utter_message(text="I'm sorry, I didn't understand your document choice.")
        elif user_choice.lower() == "barangay id":
            dispatcher.utter_message(text="The needed requirements for Barangay ID are:\n-Accomplished Application Form\n-Valid ID\n-Proof of Residency (at least 6 months)")     
        elif user_choice.lower() == "barangay clearance" or user_choice.lower() == "clearance":
            dispatcher.utter_message(text="The needed requirements for Barangay Clearance are your name, age, address, and purpose of using the Barangay Clearance.")
        elif user_choice.lower() == "certificate of indigency"  or user_choice.lower() == "indigency":
            dispatcher.utter_message(text="The needed requirements for Certificate of Indigency are:\n-Accomplished application form\n- Death Certificate (For burial purpose only)")
        elif user_choice.lower() == "business permit":
            dispatcher.utter_message(text="The needed requirements for a Business Permit are Business Owner's name, Business' Name, Business Line, and Business Address.")
        return []
    