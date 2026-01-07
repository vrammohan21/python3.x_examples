#Keys : names of the employees & Values will store the History of the related employee
nest_dict={"Dave":{"Role":"Lead","Tech":"Python","Exp":5,"CTC":13.5},
           "John":{"Role":"Manager","Tech":"Java","Exp":10},
           "Jack":{"Role":"Developer","Tech":"AI","Exp":2},
           "Timm":{"Role":"Tester","Tech":"DS","Exp":3},
           "Lucy":{"Role":"Developer","Tech":"Java","Exp":3}}#Nested Dict.
keys=list(nest_dict.keys())
#lowercase_list = list(map(str.lower, my_list)) -> using map function
#lowercase_list = [item.lower() for item in my_list] -> comprehension
#print(f"Type of nest_dict_keys ={type()}")
"""user_input=(input(f"Enter a key to search from {nest_dict.keys()}:"))
 if user_input.lower() in nest_dict.keys():
    for k in nest_dict.keys():
        if user_input==k.lower():
            #print(f"\t{k} : {nest_dict.get(k)}", end="\n")
            #print(f"keys of {nest_dict.get(k)}={nest_dict.get(k).keys()}")
            ip2=input(f"Enter your input from {nest_dict.get(k).keys()}:").lower()
            if ip2 in nest_dict.get(k).keys():
                print(f"{ip2} is mapped to {nest_dict.get(k).get(ip2)}")
            else: print(f"{ip2} is Invalid key")
else: print(f"{user_input} is Invalid key") """
