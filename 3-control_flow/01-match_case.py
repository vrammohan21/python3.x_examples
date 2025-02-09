day=input("What is today? ")
day=day.capitalize()
print(f"You have entered ....{day}")
match day:
    case 'Sunday':
        print("WOW....")
    case 'Monday':
        print("hhhhhhaaa BORING")
    case 'Tuesday':
        print("hhhaaa BORING")
    case 'Wednesday':
        print('hhaa Boring')
    case 'Thursday':
        print("ha Boring")
    case 'Friday':
        print('Reeaching SUNDAY')
    case 'Saturday':
        print('Hey.............')
    case _ :
        print(f"WHO ARE YOU? Mr/Ms {day}")