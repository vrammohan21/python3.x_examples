day=(input('What is today?')).lower()
#day=day.lower()
if day=='sunday':
     print('IF-Hey HOLIDAY!!!')
elif day=='monday':
    print('ELIF--hhhhhhhh BORING DAY:)')
else:
    print("else-WAITING for SUNDAY.....")

match day:
    case 'sunday':
        print('match-Hey HOLIDAY!!!')
    case 'monday':
        print('match-hhhhhhhh BORING DAY:)')
    case 'tuesday' | 'wednesday' | 'thursday' | 'friday' | 'saturday':
        print("match-WAITING for SUNDAY.....")