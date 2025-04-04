t1=("Ram","Raj","Audi",100,89.56)
print(f"\tLength of t1 = {len(t1)} & t1[2]={t1[2]}")
t1[2]="Benz"
#Work-around to update a tuple.
#Step1: Convert the tuple into a list.
#modify - CRUD operations
#step3: convert back that modified list again to a tuple.
