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
            dispatcher.utter_message(text="The needed requirement for Barangay ID is:\n- Accomplished Application Form")     
        elif user_choice.lower() == "barangay clearance" or user_choice.lower() == "clearance":
            dispatcher.utter_message(text="The needed requirement for Barangay Clearance is: \n- Accomplished Application Form")
        elif user_choice.lower() == "certificate of indigency"  or user_choice.lower() == "indigency":
            dispatcher.utter_message(text="The needed requirements for Certificate of Indigency are:\n- Accomplished application form\n- Death Certificate (For burial purpose only)")
        elif user_choice.lower() == "business permit":
            dispatcher.utter_message(text="The needed requirement for a Business Permit is: \n- Accomplished application form.")
        else:
            dispatcher.utter_message(text="I'm sorry, I didn't understand your document choice.")
        return []

class FilDocumentRequirements(Action):
    def name(self) -> Text:
        return "f_requirements_needed"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_choice = tracker.get_slot("document")

        if user_choice is None:
            dispatcher.utter_message(text="Paumanhin, ngunit hindi ko maintindihan ang napiling dokumento mo.")
        elif user_choice.lower() == "barangay id":
            dispatcher.utter_message(text="Ang kinakailangang requirement para sa Barangay ID ay:\n- Naisagawang Application Form")     
        elif user_choice.lower() == "barangay clearance" or user_choice.lower() == "clearance":
            dispatcher.utter_message(text="Ang kinakailangang requirement para sa Barangay Clearance ay:\n- Naisagawang Application Form")
        elif user_choice.lower() == "certificate of indigency"  or user_choice.lower() == "indigency":
            dispatcher.utter_message(text="Ang mga kinakailangang requirements para sa Certificate of Indigency ay:\n- Naisagawang application form\n- Death Certificate (Para lamang sa mga burial ang layunin")
        elif user_choice.lower() == "business permit":
            dispatcher.utter_message(text="Ang kinakailangang requirement para sa Business Permit ay:\n- Naisagawang Application Form")
        else:
            dispatcher.utter_message(text="Paumanhin, hindi ko maintindihan ang napiling dokumento mo.")
        return []
    