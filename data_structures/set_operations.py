#Set operations
#set features:
    #Mutable , un-ordered , Unique elements (No Duplicates)
s1={100,3,0,-2,55}
s2={100,4,900,5}
""" print(f"\t| gives the union of sets : {s1|s2}")#union of sets
print(f"\t & gives the intersection of sets : {s1&s2}")#intersection-common elements
print(f"\t - gives the difference of sets : {s2-s1}")#difference (from s1 but not in s2) """
""" print(f"\t| gives the union of sets : {s1.union(s2)}")#union of sets
print(f"\t & gives the intersection of sets : {s1.intersection(s2)}")#intersection-common elements
print(f"\t - gives the difference of sets : {s2.difference(s1)}")#difference (from s1 but not in s2)
print(f"\t{s1}& {s2} and s1^s2 = {s1^s2}")#Symmetric difference or complement of the intersection
s3={100,3,0,-2}
 if s3<s1: #sub-set or super-set, we can use <,<=,>,>=
    print(f"{s3} is a subset of  {s1} ")
elif s3>s1:
    print(f"{s3} is a superset of  {s1} ")
if s1>=s1: #sub-set or super-set, we can use <,<=,>,>=
    print(f"{s1} is a subset of  {s1} ")
elif s1<=s1:
    print(f"{s1} is a superset of  {s1} ")
 """
set4={1,2,3,4,5}
print(set4)
set4.update(2)
print(set4)
