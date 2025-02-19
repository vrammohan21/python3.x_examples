#COMPARISON OPERATORS ARE USED TO COMPARE 2 VARIABLES / VALUES.
num1= int(input("Enter number1: "))
num2= int(input("Enter number2: "))
# > < >= <= == !=
if num1>num2 :
    print(f"{num1} is GREATER THAN {num2}")
elif num1==num2:
    print(f"{num1} is EQUAL to {num2}")
elif num1<num2 :
    print(f"{num1} is LESS THAN {num2}")
elif num1>=num2:
    print(f"{num1} is GREATER or EQUAL to {num2}")
elif num1<=num2:
    print(f"{num1} is LESS or EQUAL to {num2}")
elif num1!=num2:
    print("{num1} is NOT EQUAL to {num2}")
