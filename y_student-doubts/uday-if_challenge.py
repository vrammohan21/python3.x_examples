STD=int(input("Enter the percentage of the Student:"))
print("The Student percentage is=",STD)
if STD>=90:
    print("Grade = A for",STD,"%")
elif STD>=80:
    print("Grade = B for",STD,"%")
elif STD>=70:
    print("Grade = c for",STD,"%")
elif STD>=60:
    print("Grade = D for",STD,"%")    
elif STD>=40:
    print("Grade = PASS for",STD,"%")
else:
    print("Grade = FAIL for",STD,"%")