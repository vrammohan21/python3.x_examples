'''Slicing is an operation done on any SEQUENCE TYPE
to obtain elements(single/multiple), but mostly Multiple elements
from the sequence type.
Slicing can be done by using indices.
: is the symbol used for slicing.
[<START_INDEX> : <END_INDEX>] here <END_INDEX> is EXCLUDED.
example- [2:6] this returns a elements of a list from index 2 till 5.
'''
my_list=[1,2,4,6343,232,'slicing',True,101.86]
#Slicing with start & end indices
print(f"{my_list} sliced from index 1 to index 4= {my_list[1:5]} ")
#if END INDEX is not mentioned, list is sliced from start index till the end
print(f"{my_list} sliced from index 1 to last index {my_list[1:]} ")
#if START INDEX is not mentioned, list is sliced from first index till the END_INDEX value
print(f"{my_list} sliced from first index of the list till index 6 {my_list[:6]} ")
#if both START & END INDEX values are not mentioned,whole list is returned
print(f"{my_list} no index mentioned, return whole list {my_list[:]} ")