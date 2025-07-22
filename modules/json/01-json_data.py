#json : Java Script Object Notation
#json: exchange/tranfer unstructructed data
#Python treats JSON data like dictionaries and lists
#json: Python has an in-built json module.

import json

capitals = {"India":"New Delhi","USA":"Washington D.C","Italy":"Rome"}
print(f"capitals variable is of type '{type(capitals)}'")
#convert 'capitals' into a json
json_obj1=json.dumps(capitals)
print(f"json_obj1 variable is of type '{type(json_obj1)}'")
print(f"json_obj1 = {json_obj1}")

fruits=['banana','apple','grapes','avacados']
#convert fruits to a json object, this is a json array
print(f"\nfruits variable is of type '{type(fruits)} & its json variant = {type(json.dumps(fruits))} &\n it looks like {json.dumps(fruits)}")
#set types are not supported here.