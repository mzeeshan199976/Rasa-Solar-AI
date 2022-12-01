# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


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
                                    2: "action_handle_self",
                                    3: "action_handle_learn_more"},
                                "benefits": {
                                     1: ("action_handle_benefits","1"),
                                     2: ("action_handle_benefits","2"),
                                     3: ("action_handle_benefits","3"),
                                     4: ("action_handle_benefits","4"),},
                                "self": {
                                     1: ("action_handle_self","1"),
                                     2: ("action_handle_self","2"),
                                     3: ("action_handle_self","3"),},
                                "learn": {
                                     1: ("action_handle_learn_more","1"),},
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
            4.  Am I ready for solar?"""

            #message=message+str(suboption) 
            dispatcher.utter_message(text=message)
            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "benefits")]
        
        elif suboption == "1":
            # We are in a submenu
            message = """
            1.  What are the financial benefits of solar energy?\n
            2.  What are the environmental benefits of solar energy?\n
            3.  How do I find out how much I pay for electricity?\n
            4.  What is net metering?"""
            #message=message+str(suboption) 
            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]
        
        elif suboption == "2":
            # We are in a submenu
            message = """
            1.  How do solar photovoltaic (PV) panels work?
            2.  Do my solar panels produce power when the sun isn't shining?
            3.  What happens if there is dust on solar panels?
            4.  Can I go off grid with solar panels?
            5.  Will I still receive an electric bill if I have solar panels?
            6.  Do solar panels work in a blackout?
            7.  How much will solar panel maintenance cost?"""

            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]
        elif suboption == "3":
            # We are in a submenu
            message = """
            1.  What solar energy rebates and incentives are available?
            2.  What are my solar financing options?
            3.  Should I buy or lease my solar panel system?
            4.  Which is better – EPC or PPA?"""
            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]
        elif suboption == "4":
            # We are in a submenu
            message = """
            1.	Can I afford to go solar?
            2.	Is my roof suitable for solar panels?
            3.	What size solar energy system should I get?
            4.	Do I need to replace my roof before installing solar?
            5.	How long will my solar power system last?
            6.	What happens if I sell my solar house?"""
            
            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)] 
           

class ActionHandleself(Action):

    def name(self) -> Text:
        return "action_handle_self"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        suboption = tracker.get_slot("suboption")
        if suboption is None:
            # We are in the main menu
            message = """“Welcome to Solar AI! We believe your journey with us will last for years to come.\n
\n 
            1.	How do I get a solar quote?\n
            2.	What services do I get with Solar AI?\n
            3.	Quick self-assessment of my solarization potential.\n
\n
Please select an option from above\n"""

            #message=message+str(suboption) 
            dispatcher.utter_message(text=message)
            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "self")]
        
        elif suboption == "1":
            # We are in a submenu
            message = """
            1.	How do I get a solar quote?\n
            2.	How accurate is the solar quote that I get from you?\n
            3.	What are the different types of solar panels?\n
            4.	What are the different types of power inverters?\n
            5.	Do I need to install solar batteries with my solar power system?\n"""
            #message=message+str(suboption) 
            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]
        
        elif suboption == "2":
            # We are in a submenu
            message = """
            1.	What is Solar Ai?\n
            2.	How can Solar AI assist me in choosing the best solar power solution?\n
            3.	What is a Customized 3D Proposal?\n
            4.	What are the benefits of choosing Solar Ai?\n
            5.	How do I contact Solar Ai?\n"""

            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]
        elif suboption == "3":
            # We are in a submenu
            message = """
            get data from user"""
            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]


class ActionHandlelearn(Action):

    def name(self) -> Text:
        return "action_handle_learn_more"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        suboption = tracker.get_slot("suboption")
        if suboption is None:
            # We are in the main menu
            message = """Welcome to Solar Ai! If you are looking to solarize your home or just stopping by for a quick assessment of the solar potential at your location, we are happy to help! Caring for our customers is our top priority.\n 
                1.	Learn more about Solar Ai\n
                2.	Learn more about my human coworkers\n
                3.	Speak to my human coworkers\n"""

            #message=message+str(suboption) 
            dispatcher.utter_message(text=message)
            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "benefits")]
        
        else:
            # We are in a submenu
            message = """My human co-worker will get in touch with you shortly! Meanwhile, please feel free to browse through the menu. Alternatively, you can visit our website to set up a remote meeting from our online calendar."""
            #message=message+str(suboption) 
            dispatcher.utter_message(text=message)

            # Indicate the submenu in which the options below will be processed
            return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]
