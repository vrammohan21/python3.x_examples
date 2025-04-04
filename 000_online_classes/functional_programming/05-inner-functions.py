def return_even(num1,num2):
    sum=num1+num2
    print(f"\tresult of outer_func={sum}")
    
    def check_even():
        print(f"\tInner_FUNCTION's sum= {sum}")
        if sum%2==0:
            return sum
        else:
            return sum*2 #return sum+1, sum-1
    return check_even()
    
number1=int(input("Enter number1:"))
number2=int(input("Enter number2:"))
print(f"\t {return_even(number1,number2)}")

""" def outer_func():
    print("\t I am an OUTER function")

    def inner_func(): #NESTED or Inner function -> function defined inside another function.
        print("I am an inner function")
   
    inner_func()#It's scope is till the outer function.

outer_func()
#inner_func()#SCOPE is with-in the function where it is defined. """