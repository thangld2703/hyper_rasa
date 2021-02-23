# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionCreateAccountValidate(Action):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "action_cust_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[
                Dict[Text, Any]]:
        # dispatcher.utter_message(template="utter_last_name")
        slots_to_validate = tracker.form_slots_to_validate()
        for slot_name, value in slots_to_validate.items():
            function_name = f"validate_{slot_name}"
            fn = getattr(self, function_name)
            fn(value, tracker, bla)
        cust_sex = tracker.get_slot('cust_sex')
        SlotSet('cust_name', tracker.latest_message['text'])
        cust_name = tracker.get_slot('cust_name')
        dispatcher.utter_message(text= " tên " + cust_sex + "là" + cust_name  )
        return [SlotSet('cust_name', tracker.latest_message['text'])]

