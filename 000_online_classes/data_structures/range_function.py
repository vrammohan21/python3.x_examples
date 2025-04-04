PI=3.14
PI=4.14
list1=[99,79,49,9,39,19]
tuple1=(99,79,49,9,39,19)
print(f"list1={id(list1)} , tuple = {id(tuple1)}")
list1.append(109)#added at the end of the list
#print(list1)
for i in range(len(tuple1)-1):
    print(tuple1[i])
""" tuple1=
print(f"list1={id(list1)} , tuple = {id(tuple1)}")
 """