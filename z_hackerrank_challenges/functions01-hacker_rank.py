def is_leap(year):
    print('in is_leap for:',year)
    leap=False
    if(year%4==0 and year%100!=0) or (year%400==0):
        leap=True
        return leap
    

def main():
    print('in main')
    year=int(input())
    leap=is_leap(year)
    print(leap)
#Run the complete problem.
main()