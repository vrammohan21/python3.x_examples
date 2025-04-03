def is_even(num1):
    msg="Invalid Input"
    flag=False
    if num1>=2:
        msg="Valid Input"
        if num1%2==0:
            flag=True
        else:
            flag=False

    return flag,msg
    
user_input=int(input("Enter a number:"))
result,msg=is_even(user_input)
if(msg!="Invalid Input"):
    print(f"{user_input} is Even {result} & about input : {msg}")
else:
    print("Please enter a valid input (GREATER THAN or EQUAL TO 2)")
