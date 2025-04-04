s='level'
s1,s2='',''
#print(len(s))
if len(s)%2!=0:
    mid=len(s)//2
    #print(f"mid is {mid}")
    for i in range(0,mid):#0,1
        s1+=s[i:mid]
    for i in range(mid,len(s)):
        s2+=s[(len(s))-1:i]
    print(f"s1 is {s1}")    
    print(f"s2 is {s2}")
    #print(s1,s2)   
    #print(s1,s2)
