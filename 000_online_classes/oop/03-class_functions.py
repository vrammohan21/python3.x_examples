class Car:
    brand="Audi"#class variables
    #default initializer is __init__(self)
    #Initializer - acts as a Contructor - instantiate a class , 'self' indicates CURRENT OBJECT
    def __init__(self,color,name,model):#instance variables
        self.color,self.name,self.model=color,name,model
        
    def __str__(self):
        return f"\tMine is a {self.brand} {self.name} car in {self.color} Color of {self.model} Model"
        
audi=Car("Shiny Black","Audi-Classic","Q8")
print(audi)# If __str__ defined in the class, it is called. Otherwise, memory address of the object is printed.

audi2=Car("Silver White","Audi-SUV","Q7")
print(audi2)

class SportzCar(Car):
    pass#Place holder

f2=SportzCar("RED","Ford-F2","F2-Sports")
print(f2)

