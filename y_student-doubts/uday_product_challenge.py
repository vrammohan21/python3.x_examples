# Sample product data
products={"Laptop": {"name": "Lenovo", "price": 75000, "in_stock": True},
         "Smartphone" : {"name": "Apple", "price": 45000, "in_stock": True},
"Headphones" : {"name": "Sony", "price": 2500, "in_stock": True},
"Smartwatch" : {"name": "Fireboltt", "price": 4500, "in_stock": True},
"Tablet" : {"name": "Samsung", "price": 30000, "in_stock": True}}
'''
#Accessing the nested values
print("The price of the Laptop is:",products["Laptop"]["price"])
print(products["Smartwatch"]["price"])
products["Smartphone"]["price"]=80000
print(products["Smartphone"]["price"])
#Output: 75000
#Display all products
print("Product List:")
for product, name in products.items():
    print(f"{product}: {name}")
#for name, price in products.items():
 #   print(f"{name}:${price}")'''

'''
print(f"\n Details:")
for key, value in products.items():
    print(f"{key}: {value}")'''

'''
print(f"Type of the products={type(products)}")
print(f"Length of the products={len(products)}")
print(f"All the keys in products = {products.keys()}\n")
print(f"All the Values in products = {products.values()}\n")
#print(f"The key Value of :{products["Headphones"]}")#
print("HeadPhone Details =",products["Headphones"])#'''

user_input=input(f"Enter a key from {products.keys()}")
if user_input in products.keys():
    for k, v in products.get(user_input).items():
        print(f"{k}: {v}")
else:
    print(f"Key '{user_input}' is Invalid, Please enter a valid key")