# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
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

class RequestDocument(Action):
    def name(self) -> Text:
        return "steps_request"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_choice = tracker.get_slot("document")

        if not user_choice:
            dispatcher.utter_message(text="I'm sorry but it seems that we don't offer that type of document.")
        elif user_choice.lower() == "barangay id":
            dispatcher.utter_message(text="If you want to request a Barangay ID, kindly check the sidebar. Click the \"Services\" button. Next, click the Document Request button and then the Barangay ID button. You will be directed to the page where you can request a barangay ID. Fill out the blank text fields and upload a picture of a valid ID or scanned copy of NSO. Lastly, click the \"Submit\" button. I hope this information works well for you. ")     
        elif user_choice.lower() == "barangay clearance" or user_choice.lower() == "clearance":
            dispatcher.utter_message(text="If you want to request Barangay Clearance, kindly check the sidebar. Click the \"Services\" button. Next, click the Document Request button and then the Barangay Clearance button. You will be directed to the page where you can request Barangay Clearance. State the purpose of your request and then click the \"Submit\" button. I hope this information works well for you. ")
        elif user_choice.lower() == "certificate of indigency"  or user_choice.lower() == "indigency":
            dispatcher.utter_message(text="If you want to request a Certificate of Indigency, kindly check the sidebar. Click the \"Services\" button. Next, click the Document Request button and then the Certificate of Indigency button. You will be directed to the page where you can request a Certificate of Indigency. State the purpose of your request and then click the \"Submit\" button. I hope this information works well for you. ")
        elif user_choice.lower() == "business permit":
            dispatcher.utter_message(text="If you want to request a Business Permit, kindly check the sidebar. Click the \"Services\" button. Next, click the Document Request button and then the Business Permit button. You will be directed to the page where you can request a Business Permit. It will require you to state the name of your business and its business line. Additionally, it will require you put the business address. After you fill out the needed information, click the \"Submit\" button. I hope this information works well for you.")
        else:
            dispatcher.utter_message(text="I'm sorry but it seems that we don't offer that type of document.")
        return []