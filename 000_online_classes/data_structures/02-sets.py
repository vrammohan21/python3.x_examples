#Features of a Set - Hashable, Un-ordered, Un-indexed, Mutable, No Duplicates.
#Set is a collection of unique elements.
set1=set()
#set1={"Ram","XYZ","ABC","Zero"}
print(f"original set1={set1}")
#remove an element from a set.
set1.remove("Ram")
print(f"Ram removed={set1}")
set1.add("IJK")
print(f"after IJK={set1} & type = {type(set1)}")
set1.add("John")
print(set1)
set1.update({"Jack","Robert"})
print(f"Updated set1={set1}")
set1.update(["honda",100])
print(f"Updated set1={set1}")
set1.update({111:2,300:4})#update method needs an ITERABLE object.
print(f"2nd time set1={set1}")
#remove(<value>) vs discard(<value>): remove raises an exception if the value is not found.
#discard does not raise an exception if the value is not found.
#set1.remove('ABC')
set1.discard("ABC")
print(f"ABC removed={set1}")
#set1.remove('ABC')#your Program STOPs here.
set1.discard("ABC")
print(f"discarding ABC={set1}")
x=set1.pop()
print(f"{x} is poped out={set1}")
set1.clear()
print(f"cleared set1: {len(set1)} & {set1}")
#Accessing elements of a set
""" for s in set1:
    print(s) """
#print(f"set1={type(set1)}")
#print(f"Amount of data : {len(set1)}")