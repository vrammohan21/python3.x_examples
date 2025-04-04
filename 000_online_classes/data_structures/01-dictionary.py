orders ={123:"Laptop", 124:"Mobile", 125:"Tablet"}
#print(type(orders))
#access a dictionary using
    #keys , #values, items (key-value) pairs , get() 

""" print(f"All the keys of my dictionary = {orders.keys()} , & type of keys is {type(orders.keys())}")
print(f"values = {orders.values()}")
print(f"Dictionary key-value pairs = {orders.items()}") """
k=orders.keys()#Returns an iterable type - > Collection (tuple)
for k in orders: # k is non iterable since it is an integer object.
    print(f"value mapped with {k} is {orders[k]}")
    #print(f"\t k-v: {k}-{get(k)&key_type= {type(k)}&value type = {type(v)}",end='')


    