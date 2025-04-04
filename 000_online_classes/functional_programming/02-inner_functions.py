def sum(a,b):
    c = a+b
    def sum_inner(x):#nested function.
        return x*2
    
    return sum_inner(c)
    #return y

print(f"{sum(4,5)}")