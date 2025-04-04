#Packing & Unpacking tuples.
#Packing means : tup1=("Ram","raj",100,89.56) -> create a tuple, assign values.
#Extraction: Unpacking / accessing values of the tuple & assign them to some other variables.
#access using: index(+ve,-ve). Also slicing.
t1=("Ram",100,"Audi",89.56)
print(f"\tLength of t1 = {len(t1)}")
# * allows to assign multiple values in to a single variable.
# * is used to extract the remaining values.
# a,b,*c=t1 #output: a=Ram,b=100,c=("Audi",89.56)
print(f"\ta={a},{type(a)} & b={b},{type(b)} & c= {c} & {type(c)}")
if(type(a)==float):
    print(f"a is a string & it's value = {a}")
elif type(b)==str:
    print(f"b is an integer & b={b}")
else:
    print(f"c got all the other values {c}")
#print(f"\ta={a},{type(a)} & b={b},{type(b)} & c= {c} & {type(c)}")