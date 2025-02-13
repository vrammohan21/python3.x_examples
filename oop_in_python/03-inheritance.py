#I am the Parent
class Pet:
    def __init__(self,name,age): #Constructor used for initialization & self is the instance of the class
        self.name=name
        self.age=age

    def pet_details(self):
        print(f"My Pet name={self.name} & it's age={self.age}")

    def move(self):
        return "I'm moving"
    def speak(self):
        return "I'm speaking"

#Inherit the Pet
class Cat(Pet):
    def speak(self):
        return "Meow : I'm speaking"
    def move(self):
        return "I'm a cat, I jump onto/from the walls"

#Inherit the Pet
class Dog(Pet):
    def speak(self):
        return "Bowwwww bowh : GOT it...."
    def move(self):
        return "I run like anything"

p=Pet("Pet",5)
p.pet_details()
print(p.move())
cat1=Cat("rosy",10)
cat1.pet_details()
print(cat1.speak())
dog1=Dog("Jimmy ",15)
dog1.pet_details()
print(dog1.move(),dog1.speak())