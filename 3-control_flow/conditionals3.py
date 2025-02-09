def main():
    num=int(input("Enter a number:"))
    if _is_even(num):
        print(num,"is Even Number")
    else: print(num,"is ODD number")
#define a function to find if a number is EVEN or NOT
def _is_even(n):
    if n%2==0:
        return True
    else : return False

main()
