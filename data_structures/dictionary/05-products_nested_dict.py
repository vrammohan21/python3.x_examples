#Products is a nested dictionary
products={"Laptop": {"name": "Lenovo", "price": 75000, "in_stock": True},
         "Smartphone" : {"name": "Apple", "price": 45000, "in_stock": True},
"Headphones" : {"name": "Sony", "price": 2500, "in_stock": True},
"Smartwatch" : {"name": "Fireboltt", "price": 4500, "in_stock": True},
"Tablet" : {"name": "Samsung", "price": 30000, "in_stock": True}}

#Display all products

for product, name in products.items():
    print(f"{product}: {name}")

user_input=input(f"Enter a key from {products.keys()}:")
if user_input in products.keys():
    for k, v in products.get(user_input).items():
        print(f"{k}: {v}")
else:
    print(f"Key '{user_input}' is Invalid, Please enter a valid key")