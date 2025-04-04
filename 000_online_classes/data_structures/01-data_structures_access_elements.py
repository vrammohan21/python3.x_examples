#tuple
event=("Ram","Uday","Modi","RevanthReddy","Uday")
""" print(f"event={type(event)}")
print(f"length={len(event)}")
print(f"Count of Uday={event.count("Uday")}")
print(f"Count of ram={event.count("Ram")}") """

#Count gives the 'count of the element passed as a parameter in the called object.
#Count gives how many times it's parameter is present in the object.
name="Hello World Hello"
#print(f"\tcount of 'l' in {name}={name.count("Hello")}")

set2={"Ram","Uday","Modi","RevanthReddy","Uday"}
#set1={"Ram",0,100,1,True,False,74.34}
set1={"Ram",0,100,False,1,True,74.34}#Un-Ordered,Un-Indexed,No Duplicates,Mutable
#print(f"\n\t set1 ={set1}")#Ram,0,100,1,74.34

admissions=frozenset({False,0,1,4,2,3,4,True})
print(f"\tType of admissions={type(admissions)} & len={len(admissions)}\n\t{admissions}")
for a in admissions:
    print(a,end=" ")
""" if True == 1:
    print(f"True == 1") """
#print(f"\n\t set1 type={type(set1)} & length of set1={len(set1)}")


#List
l1=["Ram","Uday",100,74.34,True]
#print(f"l1 is a {type(l1)}")
#print(f"\tcount of l1={len(l1)}")#indices: +ve: 0-4 ,-ve index(starts from the reverse): -1 to -5
""" print(f"\t{l1[2]}")#Only the element at the mentioned index is accessed.
print(f"\t\t{l1[-2]}")#Only the element at the mentioned index is accessed.
 """#Slicing: used to access multiple elements of the list based on start&end indices.
#print(f"\t{l1[:100]}")#index: o,1,2(end_index-1) -> Means the end-index is not included.
#1.The slicer will count the length - 5
#2. The slicing operation happens till the last index available in the above (100)
# if end_index>len : it will consider elements till the end index of the list.

