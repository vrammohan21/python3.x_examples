n=int(input("Number?"))
ch=input('Enter the character you wanna print:')
for row in range(n):
    print(ch,end='')
    for col in range(row):
        print(ch,end='')
    print()