# Let's start the NESTED LOOPs.
"""
What's a Nested loop: "A loop that stays inside another loop"
    1.Loop that contains another loop
    2.Outer loop contains inner loop.
    for i in range(n):
        <EXTERNAL_LOOP_CODE>
        for j in range(m):
            <INNER_LOOP_CODE>
 """
num=int(input("How Many?"))

#external loop
for row in range(num): # if start =1, then the end should be num+1 for both the loops, as the loop starts(default=0) & end_value is
    for col in range(num):
        print('*',end="")
    print()
