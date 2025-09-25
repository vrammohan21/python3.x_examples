msg='''
    Hello User! Please Select an option from below:
        1 - Deposit.
        2 - With Draw Money
        3 - Check Your Balance
        4 - Exit
'''
choice=int(input(msg+" :"))
options=[1,2,3,4]
bal=10000
while True:
    if choice not in options :#EDGE CASE or VALIDATION
        choice=int(input("Please enter any of 1/2/3/4:"))
    elif choice==1:
        money=float(input("Please enter the amount & put the amt in m/c closet:"))
        bal+=money
        print(f"Deposited {money}& ur current balance={bal}")
    else:
        print("Hello")

    break