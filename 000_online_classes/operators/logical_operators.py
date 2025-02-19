#and or not
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
#elif num1==0 or num2==0:
#    print("result is zero & NO SIGNIFICANCE for the sign")
 