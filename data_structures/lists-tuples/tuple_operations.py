#Tuple is another sequential data type in python similar to List.
#Only difference b/w List & Tuple is : Tuple is IMMUTABLE
#Tuple is created by using parenthesis '(' and ')'
#create a tuple
even_nums=(10,4,21,6,8,-1,2,2)
print(type(even_nums))
print(even_nums)
#tuple operations:
print(f"Count of 2 = {even_nums.count(2)}")
print(f"Index of 2 = {even_nums.index(2)}")
print(len(even_nums))