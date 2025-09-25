s1={}#Empty set,main priority will be given & this will be treated as a dictionary
print(f"Type of s1={type(s1)}")
s2=set()#set constructor
print(f"Type of s2={type(s2)}")
#s3={"John","Jack","Lucy",[1,2,3],(True,False)}#ERROR: LIST is NOT-Hashable, so can't add it to a SET.
s3={"John","Jack","Lucy",(True,False)}#Removing the list will correct the program
print(f"Type of s3={type(s3)}&s3={s3}")
#ADD elements to a set in 2 ways: add(el_name) for single element & update(elements) for Multiple elements
s3.add("AI")
print(f"After add operation, s3 = {s3}")
s3.update([1,2,3])
print(f"After UPDATE operation, s3 = {s3}")
#Removing elements from a set 4 ways: remove(),discard(),clear(),pop()
s3.remove(3)
print(f"After Removing 3,s3={s3}")
print(f"After Discarding 2,s3={s3.discard(2)}, s3={s3}")
print(f"After poping={s3.pop()}, s3={s3}")
#clear can be seen at the end : s3.clear()
print