class Phone():
    color,size,camera,brand=None,None,None,None
    #self indicates current object.
    def __init__(self,color,size,camera,brand):
        print("\tInitializing a phone.....")
        self.color=color
        self.size=size
        self.camera=camera
        self.brand=brand
    
    def phone_details(self):
        print(f"My phone={self.brand},color={self.color},screen size={self.size} inches,camera ={self.camera} Pixels")

    def make_call(self):
        print(f"I am Calling")

    def send_msg(self):
        print("Sending message")

class FeaturePhone(Phone):
    
    def __init__(self,color,size,camera,brand):
        print("\tInitializing FeaturePhone.....")
        self.color=color
        self.size=size
        self.camera=camera
        self.brand=brand

    def make_call(self):
        print(f"1.Dial the number 2.Press the GREEN BUTTON to call.")

""" def __init__(self):#dOUBLE underSCORE -> dunder methods.
        print("Initializing....Feature Phone") """
    

class SmartPhone(Phone):
    def __init__(self, color, size, camera, brand):
        super().__init__(color, size, camera, brand)#super() - keyword, indicating parent class
        
    def make_call(self):
        print(f"1.Unlock the phone 2.open call app 3.select the number 4.Touch it to call")
        
ff=FeaturePhone('Black',2,1,"Nokia")
ff.make_call()

sp=SmartPhone("Ocean Green",6.5,60,"OnePlus")
sp.make_call()
#sp.phone_details()

#print(f"My phone={self.brand},color={self.color},screen size={self.size} inches,camera ={self.camera} Pixels")
