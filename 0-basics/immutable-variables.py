""" age=18
print('age=',age,'age address=',id(age))
age+=18
print('age+=18 now: ',age,'age address=',id(age))
age=38
print('age=',age,'age address=',id(age))
print('age=',age,'age address=',id(age))
age=48
print('age=',age,'age address=',id(age))
name='john'
print('name=',name,'name address=',id(name))
name='johnny'
print('name=',name,'name address=',id(name)) """

ids=(1,2,3)
print(f"ids type={type(ids)} & Loc of ids = {id(ids)}")
#ids[2]="Ram" #Error, tuple can't be modified
ids=("Python","Java","AI")#Re-Assignment, this is possible but, this ids object will have a DIFFERENT Memory Address.
print(f"CHANGED:ids type={type(ids)} & Loc of ids = {id(ids)}")