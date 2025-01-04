def main():
    marks = int(input("Your marks?"))
    _find_grade(marks)

def _find_grade(marks):
    
    if marks>=90:
        print("Grade A")
    elif marks>=80:
        print("Grade B")
    elif marks>=70:
        print("Grade C")
    elif marks>=60:
        print("Grade D")
    else : print("Grade E")

#call the main
main()