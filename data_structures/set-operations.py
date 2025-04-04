#set is MUTABLE , UNORDERED group of UNIQUE elements.
#set can contain ONLY IMMUTABLE elements like numbers,strings, tuples.
set1={1,'python',3.4,'Java'}
print(set1)
#add new element to set
set1.update('AI')
print("after adding AI:",set1)
set2=set('python','ai','java')
print(type(set2))
print("set2=",set2)
set2.update('AI-')
print("updated set=",set2)
#set can also be created with the set() constructor
#set2=set('ram',18)#this will give an error as we passed 2 arguments.
#print(set2)
