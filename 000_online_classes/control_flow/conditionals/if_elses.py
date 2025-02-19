color = input("Enter the color {3 options are red/green/orange}: ").upper()

if color!="" and color in ["RED", "GREEN", "ORANGE"]:
    if color == "RED":
        print("STOP")
    elif color == "GREEN":
        print("GO")
    else:
        print("WAIT")
else:
    print("INVALID input")
