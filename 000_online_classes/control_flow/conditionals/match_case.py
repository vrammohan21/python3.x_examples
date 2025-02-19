#match-case was introduced in Python 3.10
#similar swaitch-case in other languages like Java
today=input("Enter the day of the week: ").upper()

match today:
    case "MONDAY" | "TUESDAY" | "WEDNESDAY":#| is OR operator called as a pipe symbol.
        print("BORING....")
    case "THURSDAY" | "FRIDAY":
        print("Awaiting SUNDAY")
    case "SATURDAY":
        print("EAGER for SUNDAY")
    case "SUNDAY":
        print("haaaa HOLIDAY...")
    case _:
        print("Invalid input")


'''color = input("Enter the color {3 options are red/green/orange}: ").upper()
match color:
    case "RED":
        print("STOP")
    case "GREEN":
        print("GO")
    case "ORANGE":
        print("WAIT")
    case _:#default case
        print("INVALID input")
'''
