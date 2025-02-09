#string methods/functions/operations
str1=input("Enter your name:")
print("Original String:",str1)
print("Capitals:",str1.capitalize())#change the string to Capital case.
print("lower",str1.lower())#change the string case to lower case.
print("Upper",str1.upper())#change the string case to UPPERCASE.
#print("sdfds\"",str1.strip(),"\"")
#Type conversion&operation with the f string.
dollars=100
val=float(input("What is today's dollar to Rupee value?"))
#print(type(val))
print(f"Today's value of your {dollars}$ = {dollars*val:0.3f}")#formatted string.
