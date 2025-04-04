set1={"VR",'1',True,24.98,'0',False}#supports different data types

print(f"{set1} & type of set1 is {type(set1)}")
""" print(f"Length of set1 is {len(set1)}")
#add element to set
print(f"Adding element to set1")
set1.add(1)
print((f"Added 1 = {set1}"))
set1.add("Jack")
print(f"Added jack = {set1}")
set1.add("Ram")#Let's see if it adds duplicate element
print(f"Added Ram = {set1}")
set1.remove(1)
print(f"Removed 1 = {set1}")
set1.discard(1)
print(f"tried to Remove 1 = {set1}")
set1.pop()
print(f"poped out = {set1}")
 """
#Accessing elements of a set
x,y=None,None
#if '1' and '0' in set1 and '1'.isdigit():
""" for s in set1:
    if type(s)!=int and type(s)!=float and type(s)!=bool and s.isdigit():
            x=s
            y=s
    else:
            print(s)
 """
for s in set1:
    if type(s)==str and int(s)==1:
           print(s)
    elif type(s)==int and s.isdigit() :
           x=s
           print(f"x={x}")
    elif type(s)==int and s.isdigit() and int(s)==0:
           y=s
print(f"x={x} , y={y}")
    #print(s)