def intialize_employee():
   employee={}
   hours_worked = float(input("Enter the number of hours worked in a week (30-100 hrs): "))
   pay_style=int(input(f"Select the payment option (1: weekly, 2: every 2 weeks, 3: every 4 weeks):  "))
   employee['hours_worked'] = hours_worked
   employee['pay_style'] = pay_style
   return employee
def validate_employee_options(employee):
   if employee is None:
       return False
   hours = employee['hours_worked']
   pay = employee['pay_style']
   if hours < 30 or hours > 100:
       print("Hours worked must be between 30 and 100 hours based on intial agreement.")
       return False
   if pay not in pay_options:
       print("Invalid payment option. Choose from 1, 2, 3 or 4")
       return False
   return True
def calculate_employee_pay(employee):
   hours = employee['hours_worked']
   pay = employee['pay_style']
  
   if hours < 30:
       pay_rate = 90
       tax = 0 
   elif hours == 40:
       pay_rate = 110
       tax = 0 
   elif hours > 50 and hours <= 100:
       pay_rate = 150
       tax = 0.20 
   elif hours > 40 and hours<= 50:
       pay_rate = 120
       tax = 0.05 
   else:
       pay_rate = 100
       tax = 0 


   base_pay = hours * pay_rate
  
   total_pay = base_pay - (base_pay * tax)
  
   if pay == 1:
       payout_period = "Weekly"
   elif pay == 2:
       payout_period = "Every 2 weeks"
       total_pay *= 2 
   elif pay == 3:
       payout_period = "Every 3 weeks"
       total_pay *= 3
   elif pay == 4:
       payout_period = "Every 4 weeks"
       total_pay *=4 
  
   return total_pay, payout_period




pay_options = (1,2,3,4)
employee = intialize_employee()
employee_validation = validate_employee_options(employee)
if employee_validation :
   total_pay, payout_period = calculate_employee_pay(employee)
   print(f"Employee's total pay for {payout_period} is INR {total_pay:.2f}")
else:
   print("Invalid employee details. Please try again")