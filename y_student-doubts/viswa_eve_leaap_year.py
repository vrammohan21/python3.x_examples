year=int(input("enter valid year:"))
if year % 4 == 0 and year%100!=0 or year % 400 == 0  :
    print(year,"idhi leap year bro")
else:
    print(year,"idhi leap year kadhu bro")