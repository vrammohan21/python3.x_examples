def outer_func(num1,num2):
    sum=num1+num2
    def inner_func():
        if sum%2==0:
            return sum
        else: return sum*2
    return inner_func()

number1=int(input("Enter First Number:"))
number2=int(input("Enter Second Number:"))
print(f"\t{outer_func(number1,number2)}")