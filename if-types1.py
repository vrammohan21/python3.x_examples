#num=int(input("Enter one number:"))
num=10.56
print(num)
if(type(num)==int):
    print(f"{num} is an integer")
elif(type(num)==float):
    print(f"{num} is a float")

'''
if(num.isDigit()):
    print(f"{num} is a number")
    if(num%1==0):
        print(f"{num} is NOT floating point number")
    else : print(f"{num} is a float")

if num>0:
    if num%2==0:
        print(num," is even")
    #if num%2!=0:
    else:
        print(num,"is ODD number")'''