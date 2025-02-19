# Description: This function checks if a string is a palindrome or not.
def is_palindrome(s):
    return s == s[::-1]# ::-1 is a slicing trick to reverse a string

def is_palindrome2(s):
    list_s = list(s)
    for i in range(len(list_s) // 2):
        if list_s[i] != list_s[-i - 1]:
            return False
        return True
def is_palindrome3(s):
    s1=list(s)
    s1=s1[:]
    #print(f"I reversed {list(s)[:]}")
    print(f"Original string: {s} converted to list &sliced: {s1}")
    
# Get user input and check if it's a palindrome
user_input = input("Enter a string to check if it's a palindrome: ")
is_palindrome3(user_input)
#print(f"{user_input} is a palindrome: {is_palindrome2(user_input)}")