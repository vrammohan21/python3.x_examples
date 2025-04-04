list1=[100,"John",89.76,True]#Any Data type
list2=[100,200,[300,'Ram'],[400,500],True]#List of lists
#nested loops 
#print(type(list1))
l3=list1+list2#joining the lists.
print(f"{l3} is at {id(l3)}")
#list operations
l3.append("Vasu")#adding an element to the list
print(l3)
l3.insert(-3,"Sumit")
print(l3)
l3.insert(3,"Amiti")
print(l3)
l3.insert(-4,3.24444)
print(l3)
l3.remove("Sumit")
print(l3)
del l3[2]#deleted element is NOT returned.
print(l3)
j=l3.pop(2)#deleted element is returned. -> a return type
print(l3)
#sort operation.
l4=[400,900,1000,100,1900]
print(f"Original l4={l4} ")
l4.sort()
print(f"sorted ={l4}")
l4.sort(reverse=True)
print(f"Reverse sorted ={l4}")
l4=[400,900,1000,100,1900]
l5=[22,90]
l4.extend(l5)
print(f"l4 Extends l5. New l4 is {l4}")
print(f"l4+l5 leads to :{l4+l5}")

""" print(id(l3))
name="John" #string is IMMUTABLE
print(name,id(name))
name="Ram"#
print(name,id(name))
 """""" for l in list1:
    print(f"l={l} & its type={type(l)}")
 """
""" for a in list2:
    if(type(a)==int):
        continue#ignoring all the ints in the main list.
    print(f"a={a} & its type={type(a)}")
    if(type(a)==list):
        for b in a:
            print(f"b={b} & its type={type(b)}")
    #print(list2) """