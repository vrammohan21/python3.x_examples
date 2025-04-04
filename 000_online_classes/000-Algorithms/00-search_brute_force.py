#Take out an element, compare it with the element you wanted, take it if it matches with yours or go to the NEXT and REPEAT. -> TC = O(n)
#This Search, Brute Force is a random search algorithm that searches for a solution to a problem by trying all possible solutions until it finds one that works. It is a simple and straightforward approach, but it can be very inefficient for large problems.
# It is often used as a baseline for comparison with more advanced algorithms.
l1=[]
for i in range(1,10000,13):
    l1.append(i)
print(f"l1 is a {type(l1)} & length of l1={len(l1)}")

while True:
    user_input=int(input("Enter the number to be searched: "))
    if user_input >10000 and user_input < 1 :
        print(f"Please enter a number between 1 and 10000")