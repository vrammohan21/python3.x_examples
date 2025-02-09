today=input("What day is today?")

match today:
    case 'sunday':
        print("Hey Today is HOLIDAY")
    case 'monday':
        print("boring day")
    case 'tuesday' | 'wednesday' | 'thursday' | 'friday':
        print("Hey Today is HOLIDAY")
    case 'saturday':
        print("WAITING FOR SUNDAY")
    case _:
        print("invalid input")  
