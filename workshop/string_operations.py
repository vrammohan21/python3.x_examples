user_input = input("Enter a string : ")
print(f"Hello {user_input}!")
print(f"length of user_input is {len(user_input)}")#length of string
print(f"user_input in upper case {user_input.upper()}")#Convert ur string into upper case
print(f"user_input in lower case {user_input.lower()}")#convert ur string into lower case
print(f"user_input in title case {user_input.title()}")#convert ur string into title case
print(f"user_input in capitalize case {user_input.capitalize()}")#convert first char into upper
print(f"user_input in swap case {user_input.swapcase()}")#swap case converts upper to lower & viceversa
#Accessing chars of ur string using index (+ve,-ve & more than one char using slicing op)
print(f"first letter of user_input is {user_input[0]}")#accessing chars of ur string using +ve index
print(f"last letter of user_input is {user_input[-1]}")#accessing chars of ur string using -ve index
"""  : is the slicing operator.
slicing operation is used to access more than one char from ur string. """
print(f"Slicing user_input from 0 to 3: {user_input[0:3]}")#accessing more than one char using slicing op
print(f"slicing user_input from -3: {user_input[-3:]}")#accessing more than one char using slicing op
print(f"slicing user_input from start till 3: {user_input[:3]}")#accessing more than one char using slicing op
print(f"slicing user_input from -3 to -1 {user_input[-3:-1]}")#accessing more than one char using slicing op
print(f"{user_input} is alphanumeric : {user_input.isalnum()}")#check if string is alphanumeric
print(f"{user_input} is alphabetic : {user_input.isalpha()}")#check if string is alphabetic
print(f"{user_input} is digit : {user_input.isdigit()}")#check if string is digit
print(f"{user_input} is lower : {user_input.islower()}")#check if string is lower
print(f"{user_input} is upper : {user_input.isupper()}")#check if string is upper
print(f"{user_input} is title : {user_input.istitle()}")#check if string is title
print(f"{user_input} is space : {user_input.isspace()}")#check if string is space
print(f"{user_input} is printable : {user_input.isprintable()}")#check if string is printable
print(f"{user_input} is startswith : {user_input.startswith('H')}")#check if string starts with H
print(f"{user_input} is endswith : {user_input.endswith('!')}")#check if string ends with !
print(f"{user_input} is in : {'H' in user_input}")#check if H is in user_input
print(f"{user_input} is not in : {'H' not in user_input}")#check if H is not in user_input
print(f"splitting {user_input} : {user_input.split()}")#splitting the string
print(f"splitting {user_input} using ! : {user_input.split('!')}")#splitting the string using !
print(f"joining {user_input} using ! : {'!'.join(user_input)}")#joining the string using !
print(f"joining {user_input} using ! : {'!'.join(user_input.split())}")#joining the string using !
print(f"replacing {user_input} using ! : {user_input.replace('!','')}")#replacing the string using !