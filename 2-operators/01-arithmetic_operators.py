#Arithmetic Operators perform calulations / mathematical operations
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

#Confirm datatypes of two numbers.
#print(f"Datatypes of {num1}&{num2}={type(num1)} & {type(num2)}")
#Perform arithmetic operations.
#OP1-Addition
print(f"Sum of {num1} & {num2} = {num1+num2}")
#2.Subtraction
print(f"Subtraction {num2} from {num1}= {num1-num2}")
#3.Multiplication
print(f"Multiply {num1} with {num2}= {num1*num2}")
#Division
print("%.1fDivide {num1} with {num2}= %{num1/num2}")
print(f"Convert Division result into integer {num1} with {num2}= {int(num1/num2)}")#Get the integer remainder
#Exponent OR pow
print(f"Power of {num1} raised to {num2}={num1**num2}")
print(f"Using the pow function {pow(num1,num2)}")
#Modulo - Maintains the sign of the divisor.
print(f"Modulus of {num1},{num2}={num1%num2}")
#Floor Division
print(f"Floor Division of {num1} with {num2} = {num1//num2}")
