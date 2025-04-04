#Keys : names of the employees & Values will sstore the History of the related employee
nest_dict={"Ram":{"Role":"Lead","Tech":"Python","Exp":5,"CTC":13.5},
           "John":{"Role":"Manager","Tech":"Java","Exp":10},
           "Jack":{"Role":"Developer","Tech":"AI","Exp":2},
           "Timm":{"Role":"Tester","Tech":"DS","Exp":3},
           "Lucy":{"Role":"Developer","Tech":"Java","Exp":3}}#Nested Dict.

user_input=(input(f"Enter a key to search from {nest_dict.keys()}:"))
if user_input in nest_dict.keys():
    for k in nest_dict.keys():
        if user_input==k:
            #print(f"\t{k} : {nest_dict.get(k)}", end="\n")
            #print(f"keys of {nest_dict.get(k)}={nest_dict.get(k).keys()}")
            ip2=input(f"Enter your input from {nest_dict.get(k).keys()}:")
            if ip2 in nest_dict.get(k).keys():
                print(f"{ip2} is mapped to {nest_dict.get(k).get(ip2)}")
            else: print(f"{ip2} is Invalid key")
else: print(f"{user_input} is Invalid key")