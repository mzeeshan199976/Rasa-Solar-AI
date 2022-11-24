# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher

class ActionHandleOptions(Action):

    def name(self) -> Text:
        return "action_handle_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # The default value is main
        submenu = tracker.get_slot("submenu")
        option2action_name =   {"main": {
                                    1: "action_handle_benefits",
                                    2: "self",
                                    3: "learn_more"},
                                # "pytorch_version": {
                                #     1: ("action_handle_benefits", "0.x"),
                                #     2: ("action_handle_benefits", "1.x"),
                                #     }
                                }
        try:
            option = int(tracker.get_slot("option"))
        except ValueError:
            dispatcher.utter_message(text=f"Please enter a number!")
            return [SlotSet('option', None)]
        try:
            next_action = option2action_name[submenu][option]
        except KeyError:
            dispatcher.utter_message(text=f"This option is not available!")
            return [SlotSet('option', None)]

        dispatcher.utter_message(text=f"You've choosen option {option} !")

        if type(next_action) is tuple:
            return [SlotSet('option', None),
                    SlotSet('suboption', next_action[1]),
                    FollowupAction(name=next_action[0])]
        else:
            return [SlotSet('option', None),
                    FollowupAction(name=next_action)]

class ActionHandlebenefits(Action):

    def name(self) -> Text:
        return "action_handle_benefits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        suboption = tracker.get_slot("suboption")
        if suboption is None:
            # We are in the main menu
            message = """“Solar power is the last energy resource that isn't owned yet - nobody taxes the sun yet.” 🌞\n
World typically produces around 51 billion tonnes of Carbon Emissions every year, and the power sector alone contributes to about a quarter of these emissions. 💨\n
There is no path to deep decarbonization without involving the clean power sector, and there is no path to clean power without deploying significant Solar energy. ❗\n
With the increase in energy demands and grid rates, solar may be the best option for both your home and business. \n
You may select any of the following options to know more about solar energy! 👇\n
\n
            1.	Why should I go solar?\n
            2.	How do solar panels work for my home?\n
            3.	What are my solar financing options?\n
            4.	Am I ready for solar?"""

            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "pytorch_version")]
        else:
            # We are in a submenu
            message = "Here is the version {} of PyTorch"
            dispatcher.utter_message(text=message.format(suboption))

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]