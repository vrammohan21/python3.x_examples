fs1=frozenset({3,4})#IMMUTABLE
print(f"fs1 type={type(fs1)} & loc={id(fs1)}")
print(f"fs1={fs1}")
#Operations
print(f"fs1 length={len(fs1)}")
#fs1.add(0)#AttributeError
#print(f"Updated fs1={fs1}")
fs2=fs1.union({99,11})
#for s in fs2:
#    print(s,end=" ")
for s in fs1.union({99,11}):
    print(s,end=" ")



#print(f"Updated fs1={fs2}")
#Exchange -> COMPLETELY NEW CAR -> CREATING A NEW OBJECT
#PAINTING YOUR SAME CAR -> CAR IS SAME-> CHANGE THE STATE OF YOUR OBJECT




""" s1={1,2,3}#Mutable
print(f"s1 type={type(s1)} & loc={id(s1)}") """
