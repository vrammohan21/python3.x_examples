names=['ram','jawa','python']

for n in names:
    print(n)

words='python languages'
print(id(words),words)
words="Python-Changed"
print(id(words),words)
""" for w in words:
    print(w)#,end="")
    #print(*w)
    #print("".join(w))
    
count=len(names)
print("count=",count)
while count<3:
    print(names[count]) """