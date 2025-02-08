#I am the Parent
class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def my_details(self):
        print(f"My name={self.name}& age={self.age}")

#Inherit the Pet
class Cat(Pet):
    def speak(self):
        print("Meow")

#Inherit the Pet
class Dog(Pet):
    def speak(self):
        print("I BARK")

p=Pet("Pet",5)
p.my_details()
cat1=Cat("cat1",10)
cat1.my_details()
cat1.speak()
dog1=Dog("Jimmy ",15)
dog1.my_details()
dog1.speak()