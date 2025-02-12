#This example will show all the operations on a list.
my_list=[1,2,3,4]
print(type(my_list))
print(f'Original list: {my_list} ,count: {len(my_list)} & address:{id(my_list)}')
#append()- Adds an element to the list at the end
my_list.append(999)
print(f"after appending 999: {my_list} &count: {len(my_list)}")
#extend()-adds MULTIPLE ELEMENTS to my_list at the end.
my_list.extend([22,33,44])
print(f'after EXTENDING 22,33,44:{my_list} & new list count: {len(my_list)}')
#index(<ELEMENT>)-get the index of <ELEMENT> if it is in list or Gives "ValueError"
print(f'Index of the element 22:{my_list.index(22)}')
#insert() - at a specified index
my_list.insert(5,'new')
print(f"After insert operation:{my_list}")
#remove()-Removes the first MATCHING element from the list do not return any value.
print(f"after remove operation:{my_list.remove('new')}& current list={my_list}")
#pop() - removes an element at a specified index & returns the removed element.
print(f"after pop operation {my_list.pop(5)} & {my_list}")
#reverse()- reverses the list 
my_list.reverse()
print(f"after reverse operation:{my_list}")
#sort()- sorts the list : default order = ASCENDING
my_list.sort()
print(f"after sort operation in ASCENDING order:{my_list}")
#To sort in descending order
my_list.sort(reverse=True)
print(f"after sort operatin in DESCENDING order:{my_list}")
#print("address of my_list =",id(my_list))
#copy returns a shallow copy of the original list meaning that it creates a new object&returns
student_ids1=my_list.copy()
print(f"address of my_list {id(my_list)} & student_ids1 {id(student_ids1)}")
#clear() - removes all the elements from a list.
my_list.clear()
print(f"after clear() operation:{my_list} & total count:{len(my_list)} & address {id(my_list)}")
