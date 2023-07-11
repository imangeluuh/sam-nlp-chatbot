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
            dispatcher.utter_message(text="If you want to request a Barangay ID, kindly check the sidebar. Click the \"Services\" button. Next, click the Document Request button and then the Barangay ID button. You will be directed to the page where you can request a barangay ID. Fill out the blank text fields. Lastly, click the \"Submit\" button. I hope this information works well for you.")     
        elif user_choice.lower() == "barangay clearance" or user_choice.lower() == "clearance":
            dispatcher.utter_message(text="If you want to request Barangay Clearance, kindly check the sidebar. Click the \"Services\" button. Next, click the Document Request button and then the Barangay Clearance button. You will be directed to the page where you can request Barangay Clearance. State the purpose of your request and then click the \"Submit\" button. I hope this information works well for you.")
        elif user_choice.lower() == "certificate of indigency"  or user_choice.lower() == "indigency":
            dispatcher.utter_message(text="If you want to request a Certificate of Indigency, kindly check the sidebar. Click the \"Services\" button. Next, click the Document Request button and then the Certificate of Indigency button. You will be directed to the page where you can request a Certificate of Indigency. State the purpose of your request and then click the \"Submit\" button. I hope this information works well for you.")
        elif user_choice.lower() == "business permit":
            dispatcher.utter_message(text="If you want to request a Business Permit, kindly check the sidebar. Click the \"Services\" button. Next, click the Document Request button and then the Business Permit button. You will be directed to the page where you can request a Business Permit. It will require you to state the name of your business and address. After you fill out the needed information, click the \"Submit\" button. I hope this information works well for you.")
        else:
            dispatcher.utter_message(text="I'm sorry but it seems that we don't offer that type of document.")
        return []

class FilRequestDocument(Action):
    def name(self) -> Text:
        return "f_steps_request"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_choice = tracker.get_slot("document")

        if not user_choice:
            dispatcher.utter_message(text="Paumanhin, ngunit wala kaming ganitong uri ng dokumento.")
        elif user_choice.lower() == "barangay id":
            dispatcher.utter_message(text="Kung nais mong humiling ng Barangay ID, mangyaring tingnan ang sidebar. I-click ang button na 'Mga Serbisyo'. Pagkatapos, i-click ang button na 'Mag Request ng Dokumento' at pagkatapos ay ang button para sa Barangay ID. Mapupunta ka sa pahina kung saan maaari kang humiling ng Barangay ID. Punan ang mga blankong teksto. Pagkatapos, i-click ang 'Submit' na button. Sana'y gumana ang impormasyong ito para sa iyo.")     
        elif user_choice.lower() == "barangay clearance" or user_choice.lower() == "clearance":
            dispatcher.utter_message(text="Kung nais mong humiling ng Barangay Clearance, mangyaring tingnan ang sidebar. I-click ang button na 'Mga Serbisyo'. Pagkatapos, i-click ang button na 'Mag Request ng Dokumento' at pagkatapos ay ang button para sa Barangay Clearance. Mapupunta ka sa pahina kung saan maaari kang humiling ng Barangay Clearance. Isaad ang layunin ng iyong kahilingan at pagkatapos ay i-click ang 'Submit' na button. Sana'y gumana ang impormasyong ito para sa iyo.")
        elif user_choice.lower() == "certificate of indigency"  or user_choice.lower() == "indigency":
            dispatcher.utter_message(text="Kung nais mong humiling ng Certificate of Indigency, mangyaring tingnan ang sidebar. I-click ang button na 'Mga Serbisyo'. Pagkatapos, i-click ang button na 'Mag Request ng Dokumento' at pagkatapos ay ang button para sa Certificate of Indigency. Mapupunta ka sa pahina kung saan maaari kang humiling ng Certificate of Indigency. Isaad ang layunin ng iyong kahilingan at pagkatapos ay i-click ang 'Submit'' na button. Sana'y gumana ang impormasyong ito para sa iyo.")
        elif user_choice.lower() == "business permit":
            dispatcher.utter_message(text="Kung nais mong humiling ng Business Permit, mangyaring tingnan ang sidebar. I-click ang button na 'Mga Serbisyo'. Pagkatapos, i-click ang button na 'Mag Request ng Dokumento' at pagkatapos ay ang button para sa Business Permit. Mapupunta ka sa pahina kung saan maaari kang humiling ng Business Permit. Kakailanganin mong isaad ang pangalan ng iyong negosyo at ang address. Pagkatapos mong punan ang kinakailangang impormasyon, i-click ang 'Submit' na button. Sana'y gumana ang impormasyong ito para sa iyo.")
        else:
            dispatcher.utter_message(text="Paumanhin, ngunit wala kaming ganitong uri ng dokumento.")
        return []