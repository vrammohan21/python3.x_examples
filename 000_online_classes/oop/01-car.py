class Car():
    brand,color,sportz=None,None,None#initial Properties of a car

    def __init__(self,b,c,s):#initializer - this method will initialize all properties
        self.brand=b
        self.color=c
        self.sportz=s
    
    #self represents current object
    def car_details(self):
        print(f"\tcolor={self.color} & brand={self.brand}")
    def start(self):
        if self.sportz==True:
            print(f"\tSTARTING my{self.color} colored {self.brand}  car like BROOOOOOOOM")
        else: print(f"\tSTARTING my{self.color} colored {self.brand} car like mmmmmmmmmmm")
    def stop(self):
        print("STOPPING")

#Creating an (Object / instance) of car
car2=Car("BMW","Metallic Blue",True)#initialize & create the Car instance
car2.car_details()
car2.start()
#Every object got a STATE.
car3=Car("Benz","Silk Black",False)#initialize & create the Car instance
car3.car_details()
car3.start()

""" car=Car()#name="UDAY": name - variable , = assignment operator , "Uday" - value
car.brand="BMW"
car.color="Black"
car.car_details()
car.start() """




    