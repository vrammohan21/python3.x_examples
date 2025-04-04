def say_hello(name1,name2):
    print(f"\tOUTER:name1 len={len(name1)},name2 len={len(name2)}")
    
    def clean_data():
        #print(f"Inner-clean_data: {name1.strip()} {name2.strip()}")
        print(f"\tInner:name1 len={len(name1.strip())} , {len(name2)}")
    clean_data()

fname=input("Enter first name:")
lname=input("Enter last name:")

say_hello(fname,lname)

