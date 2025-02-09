student_ids=[1,2,3,4]
#print(type(student_ids))
print('Original Student IDs:',student_ids,'& Total students:',len(student_ids))
print("address of original student_ids=",id(student_ids))
#Adding a new element to the list
student_ids.append(999)
print('after appending 999:',student_ids,'&total students:',len(student_ids),id(student_ids))
student_ids.extend([22,33,44])
#extend operation: adding MULTIPLE ELEMENTS to student_ids list
print('after EXTENDING 22,33,44:',student_ids,'&total students:',len(student_ids))
#get the index of a SPECIFIC ELEMENT.
print('Index of the element 22:',student_ids.index(22))
#insert() - at a specified index
student_ids.insert(5,'new')
print("After insert operation:",student_ids)
#Removes the first MATCHING element from the list
#student_ids.remove('new')
#print("after remove operation:",student_ids)
print("after remove operation:",student_ids.remove('new'))
#pop - it removes an element at a specified index, also it returns the removed element.
print("after pop operation",student_ids.pop(5))
#reverse method reverses the list
student_ids.reverse()
print("after reverse operation:",student_ids)
#sort method sorts the list in ASCENDING order
student_ids.sort()
print("address of student_ids=",id(student_ids))
print("after sort operation in ASCENDING order:",student_ids)
#To sort in descending order
#student_ids.sort(reverse=True)
student_ids.reverse()
print("after sort operatin in DESCENDING order:",student_ids)
#copy returns a shallow copy of the original list meaning that it creates a new object&returns
student_ids1=student_ids.copy()
print("address of student_ids,student_ids1 lists:",id(student_ids),id(student_ids1))



#KEEP IT AT THE END - clearing the list
#student_ids.clear()
#print("after clear() operation:",student_ids,'total count:',len(student_ids))
