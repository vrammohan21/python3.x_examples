#Variable is a container that stores a value
name = "Python"
msg="Hello"
id=100# ORIGINAL VALUE which is an int.
#print(id,"",type(id))
'''print(name) # memory address of my variable
print("Your name",name)
print("your message=",msg)
print("Your name"+name)# here, we are concatenating the two strings.
print("Your name"+str(id))
id=str(id)#Modifying the DATA TYPE of id into a String.
print(id," ",type(id))'''

session1="Python"
start_time=5
end_time=6
duration=1
via="Google Meet"
print("Your session ",session1,"starts at",start_time,"ends at",end_time,"for",duration,"Hr, through",via)
'''Formatted string in the print statement will help us 
    to put entire message in ONE STRING
     along with the variables.
     Variables should be placed in the flower braces to get their latest values.
     Flower braces with a variable:
        Python replaces {session1} with the latest value of that variable at RUN-TIME.
'''
print(F"Your session {session1} starts at {start_time} ends at {end_time} for {duration} Hr through {via}")