def fizzBuzz(n):
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%3==0 and n%5!=0:
        print("Fizz")
    elif n%3!=0 and n%5==0:
        print("Buzz")
    elif n%3!=0 and n%5!=0:
        print(n)

var=int(input("Enter a number:"))
fizzBuzz(var)