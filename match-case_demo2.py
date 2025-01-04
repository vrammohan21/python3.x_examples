marks=int(input("Enter your marks between 0 and 100:"))
if(0<=marks<=100):
    print(marks)
    match marks:
        case x if x>=90:
            print("Grade A")
        case x if x>=80:
            print("Grade B")
        case x if x>=70:
            print("Grade C")
        case x if x>=60:
            print("Grade D")
        case x if x>=50:
            print("Grade E")
        case x if x>=35:
            print("Grade F")
        case _:
            print("Failed-You don't have a Grade")
'''else:
    print("Enter valid marks")
    '''