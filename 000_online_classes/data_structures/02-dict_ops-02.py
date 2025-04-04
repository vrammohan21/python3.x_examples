#Trying to use 'None' as a key  & also as a value in a dictionary
d2={10:"ML",20:"NLP",30:"LLM",40:None, None:"I have no Key",None:"I am a duplicate",40:"AI",30:"Python"}
#The latest key-value pair is stored in the dict object.
print(f"d2={d2}")
""" print(f"d2 keys = {d2.keys()}")
print(f"d2 values = {d2.values()}") """
#print(f"type of None = {type(None)}")
#d2.update({None:"I am a duplicate"})
print(f"d2 after update = {d2}")