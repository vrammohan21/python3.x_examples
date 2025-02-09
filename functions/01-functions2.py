#let's define our own functions
def hello(user="no input from user") :
    print("Hello",user)




hello()
name=input("what's ur name?")
if(len(name)==0):
    print("Hello User welcome.You did not entered your name")
else:
    hello(name)
#print(name)