""" 
What is Linear Search?

Linear search is a simple search algorithm used to find the position of a target (input) value within a list. It sequentially checks each element until a match is found or the list is exhausted.

Linear Search Concept and Example

Here’s a step-by-step example of how linear search works in Python for the given list [5, 4, 3, 2, 1, 10, 11, 2] and the target value “1“:

    Step 1: Start with the given list: [5, 4, 3, 2, 1, 10, 11, 2], and set the target value to 1.
    Step 2: Begin at the first element of the list, which is 5.
    Step 3: Compare 5 with the target value (1). Since they don’t match, move to the next element, which is 4.
    Step 4: Compare 4 with the target value (1). Since they don’t match, move to the next element, which is 3.
    Step 5: Compare 3 with the target value (1). Since they don’t match, move to the next element, which is 2.
    Step 6: Compare 2 with the target value (1). Since they don’t match, move to the next element, which is 1.
    Step 7: Compare 1 with the target value (1). They match! Return the index of the element, which is 4.
    Step 8: The linear search is successful, and the index 4 is returned.
    step 9: If the target value is repeated, then the INDEX OF "FIRST MATCHING ELEMENT" is returned.
 """
def linear_search(list,target):

    if target in list :
        for i in range(len(list)):
            if list[i]==target:
                return f"{target} is at the index {i}"
    else: return f"{target} is not in the list"


list=[5, 4, 3, 2, 1, 10, 11, 2]
target=int(input("Enter an element whose index you wanna find:"))
print(linear_search(list,target))

