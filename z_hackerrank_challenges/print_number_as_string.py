#if n=5, output should be 12345
# if n=3, output should be 123
n = int(input())
s=''
for n in range(1,n+1):
    s+=(str(n))
print(s)