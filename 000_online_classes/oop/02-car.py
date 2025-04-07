class Car():
    color , brand,engine_type,fuel_type=None,None,None,None
    #'self' - indicates the current object
    def display_details(self):
        #print(f"My car is a {brand} in {color} of {engine_type} with {fuel_type} tank")
        print("I display car details")
    def start(self):
        print("I am starting...")

car1=Car()
car1.display_details()#display_details(car1) , in a secured way.
car1.start()