#1-Empty class - ... means no code in the class
#2- Initializers - def will help us to start coding in the class
#3-methods - add functionality to a class
#4-None at the end of the method means that the method does not return anything
class Microwave:
    #... constructor with arguments
    def __init__(self,brand: str,rating:int)-> None:
        self.brand = brand
        self.rating = rating
        self.turned_on:bool = False
    #method-1
    def turn_on(self)->None:
        if self.turned_on:
            print(f'Microwave {self.brand}123is already turned on')
        else:
            self.turned_on=True
            print(f'Microwave ({self.brand})is just turned on')

    #method-2
    def turn_off(self)->None:
        if self.turned_on:
            print(f'Microwave ({self.brand})is just turned off')
        else:
            self.turned_on=False
            print(f'Microwave ({self.brand})is already turned off')

lg: Microwave = Microwave('LG',7)
print('brand =',lg.brand,'& rating =',lg.rating)
godrej: Microwave=Microwave('Godrej',8)
print('second microwave object',godrej.brand,godrej.rating)
print('first oop object : ',lg)
lg1: Microwave = Microwave()#This is an error, as we need to pass the brand and rating
print('second oop object : ',lg1)
lg1.turn_on()