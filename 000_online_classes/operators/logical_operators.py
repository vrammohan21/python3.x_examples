# 'and' , 'or' ,  'not' are the 3 logical operators available in Python.
# 'and' : if both conditions are true, then the result is true.
# 'or' : if any one of the conditions is true, then the result is true.
# 'not' : This operator 'inverts' the truth value. (not true = false, not false = true)
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

result= num1*num2
#MORE THAN ONE CONDITION
if num1>0 and num2>0 or num1<0 and num2<0:
    print("result is positive")
elif (num1<0 and num2>0) or (num1>0 and num2<0):
    print("result -ve")
else:
    print("result is zero & NO SIGNIFICANCE for the sign")