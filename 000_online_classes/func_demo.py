def find_even_odd():
    num1=4
    print(type(num1))

    if num1%2==0:
        print(f"{num1} is Even")
    elif num1%2!=0:
        print(f"{num1} is Odd")
    else :
        print("INVALID INPUT")

#Invoke the function
find_even_odd()