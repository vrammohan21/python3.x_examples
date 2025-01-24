#Lists & Functions
#MUTABLE & IMMUTABLE
users=[1,'name',3.5]
print('users is of type:',type(users))
print(users)
#append
users.append(4)
print('after append',users)
#create a copy of the list
users1=users.copy()
print('copy of users list:',users1)
#count the elements of the list
print('total:',len(users))
#extend() a list -> adding multiple elements to a list
users.extend([100,200])
print('after extend(100,200)',users)
#find index of a specific element.
print(users.index(200))
