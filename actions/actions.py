# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

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
#         return 
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionMakeOrder(Action):
	
	toppings = {
		"Cheese": {
			"Mozzarella": 1.50, 
			"Cheddar": 1.50, 
			"Swiss": 1.50, 
			"Provolone": 1.50
		},
		"Veggie": {
			"Pineapple": 2.00, 
			"Green pepper": 2.00, 
			"Red onions": 2.00,
			"Mushrooms": 2.00, 
			"Black Olives": 2.00
		},
		"Meat": {
			"Pepperoni": 2.50, 
			"Ham": 2.50, 
			"Bacon": 3.00, 
			"Sausage": 3.00
		}
	},
	crusts = {
		"Small": {
			"Thin": 10.00,
			"Regular": 10.00, 
			"Deep Dish": 12.00, 
			"Gluten Free": 15.00
		},
		"Medium": {
			"Thin": 12.00, 
			"Regular": 12.00, 
			"Deep Dish": 14.00, 
			"Gluten Free": 18.00
		},
		"Large": {
			"Thin": 14.00,
			"Regular": 14.00, 
			"Deep Dish": 16.00, 
			"Gluten Free": 21.00
		}
	},
	sizes = {
		"Small": 10,
		"Medium": 12, 
		"Large": 14
	},
	sides = {
		"Bread sticks": 7.00,
		"Cheese sticks": 9.00,
		"Green salad": 10.00,
		"Caesar salad": 12.00
	},
	drinks = {
		"Cola": 3.50,
		"Root beer": 3.50,
		"Orange soda": 3.50,
		"Lemon soda": 3.50,
		"Mineral water": 4.50,
		"Ginger ale": 3.50
	},
	order_type = {
		"Pick-up": 0.00
		"Delivery": 3.00
	}
	
	specials = {
		"Hawaiian" : [("Veggie","Pineapple"), ("Meat","Ham"), ("Cheese","Mozzarella")],
		"Meat Lovers" : [("Cheese","Mozzarella"), ("Meat","Pepperoni"), ("Meat","Ham"), ("Meat","Bacon"), ("Meat","Sausage")],
		"4 Cheese" : [("Cheese","Mozzarella"), ("Cheese","Cheddar"), ("Cheese","Swiss"), ("Cheese","Provolone")],
		"Pepperoni" : [("Cheese","Mozzarella"), ("Meat","Pepperoni")],
		"Veggie Supreme" : [("Cheese","Mozzarella"), ("Veggie","Green Peppers"), ("Veggie","Red onions"), ("Veggie","Mushrooms"), ("Veggie","Black olives")],
		"Vegan" : [("Veggie","Green Peppers"), ("Veggie","Red onions"), ("Veggie","Mushrooms"), ("Veggie","Black olives")]
	}
	
	

   def name(self):
      # type: () -> Text
      return "action_make_order"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

      t = tracker.get_slot('pizza_topping')
      #q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
      #result = db.query(q)
      return [SlotSet("matches", result if result is not None else [])]
	  
	  
	def special_cost(self, type):
		cost = 0
		for ingredient in specials[type]:
			category = ingredient[0]
			item = ingreditent[1]
			cost += toppings[category][item]
		return cost
		
		
	def calculate(self, type, crust, size, side, drink, in_out):
		
		final_cost = 0
		final_cost += special_cost(type)
		final_cost += crusts[size][crust]
		final_cost += sides[side]
		if drink != None:
			final_cost += drinks[drink]
		if in_out == "Delivery":
			final_cost += order_type[in_out]
		return final_cost






