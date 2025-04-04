d1={10:"Java",20:"Python",30:"AI",40:"DS"}

#Access operations - get(<KEY>) , 
print(f"get(10) = {d1.get(10)}")
print(f"get(100) = {d1.get(100)}")#If the key is not mapped, None is returned.
#keys() access all keys()
print(f"all keys = {d1.keys()} & type={type(d1.keys())}")#returns all keys & type is 'dict_keys'
#items() - access all K:V pairs
print(f"all K:V pairs={d1.items()}")
#values() - access all values of the dictionary
print(f"all values={d1.values()}")
user_input=int(input(f"Enter a key to search from {d1.keys()}:"))
#process only if the key is present in the dict.
if user_input in d1.keys():
    print(f"{user_input} is mapped to {d1.get(user_input)}")
else: print(f"{user_input} is Invalid key")

#update(<KEY>) : Update the value of an EXISTING key
#d1.update({10:"Spring Boot"})
print(f"Updated key 10={d1.update({10:"Spring Boot"})}")#checking the return type
#if the key is not present in the dict, update will create a new K:V pair
d1.update({1000:"Spring Security"})#-> Creates a new K:V pair.
print(f"update with a new key {d1}")
print(f"original value of key-20={d1.get(20)}")
#update the value of an existing key
d1[20]="Flask"
print(f"Re-mapped the key 20 to '{d1.get(20)}'")
d1[200]="Django"#200 is not available in our dict
print(f"Re-mapped the key 200 to {d1}")
#del d1[10]
#print(f"deleting key 10={del d1[10]}")
#pop(<KEY>) - removes the key and returns the value
print(f"popping 30 ={d1.pop(30)} & \n{d1}")
#popitem() - removes the last k:v pair of the dictionary
print(f"popitem1 = {d1.popitem()} & \n{d1}")
print(f"popitem2 = {d1.popitem()} & \n{d1}")
d1.clear()#removes all the data, still the object exists.
print(f"cleared d1 = {d1.clear()} & {len(d1)}")
del d1 #removes the Object itself.
