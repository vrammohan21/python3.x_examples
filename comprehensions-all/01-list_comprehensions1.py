""" #Comprehension : COMPACT than traditional SYNTAX  for generating a collection 
#Comprehensions are traditionally used in FUNCTIONAL PROGRAMMING languages to generate (most often) lists 

#syntax: newlist = [expression for item in iterable if condition == True]
list=[1,2,3,4,5,6]
new=[] """

def percentage_liked(ratings):
    #list_liked = [1, 2, 3, 4, 5, 4, 5, 1]
    # TODO: Complete the function
    ratings=[like>=4 for like in ratings]
    percentage_liked = sum(ratings)/len(ratings)
    return percentage_liked

# Do not change: should return 0.5
#print(percentage_liked([1, 2, 3, 4, 5, 4, 5, 1]))
print(percentage_liked([1, 2, 3, 4]))