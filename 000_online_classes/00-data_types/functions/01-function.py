#This code demonstrates a function definition
#a function with no parameters.
#If more than one function is defined in a file, the order of the functions does not matter,but the most latest function gets invoked.
def greet():   
    print("Hello")

def greet_the_user(cgpa):
    if type(cgpa) == float:
        print("Hello your cgpa={cgpa}")
    elif type(cgpa)==str :
        print(f"Hello {cgpa}")
    else:
        print("Invalid input")

def say_hello(name,age,cgpa):
    print(f"Hello {name} your age={age} & your cgpa={cgpa}")

name=input("Enter your name:")
age=int(input("Enter your age:"))
cgpa=float(input("Enter your cgpa:"))
print(type(name))

print(say_hello(name,age,cgpa))
print(greet_the_user(name))
#type , id , input -> print(type(name))
#say_hello(name,None,None)#None is a keyword which says that there is no value for that specific variable