class Vehicle():
    type,seats=None,None
    def __init__(self,type,seats):
        self.seats=seats
        self.type=type

    def start(self):
        pass
    def drive(self):
        pass    #keyword / placeholder -> 
#All the Properties(features or attributes) & Behaviours are (ENCAPSULATED)combined in a block of code called as 'class'.
class TwoWheeler(Vehicle):

    def __init__(self, type, seats):
        super().__init__(type, seats)

    def start(self):
        print("Unlock handle & kick the rod...")
    def drive(self):
        print("Sit on the seat & Control the handle")

class FourWheeler(Vehicle):
    def __init__(self, type, seats):
        super().__init__(type, seats)
    
    def start(self):
        print("Get in, sit in the seat,start...")
    def drive(self):
        print("Raise & Control the STEERING to drive...")

honda=TwoWheeler("Automatic",1)
honda.start()
honda.drive()

honda2=FourWheeler("AI-Based",7)
honda2.start()#Implementation details are HIDDEN - Abstraction
honda2.drive()#Implementation details are HIDDEN - Abstraction
#start(),drive() - behave differently based on the Object - Polymorphism.
""" a=input("Enter first value:")
b=input("Enter second value:")
c=a+b#+ is a concatenation operator
print(f"\t1.c={c}")

a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
c=a+b#+ addition operator.
print(f"\t2.c={c}") """