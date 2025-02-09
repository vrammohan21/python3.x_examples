#print("hello world")
name=input("what's your name?")

#using the + will concatenate whatever before&after + which will result a combined string with no spaces in between.
#print("hello"+name)

#name=name.split()

#strip() method removes leading&trailing spaces from the string it was called.
#capitalize() method converts first letter of the first word into uppercase.
#title() method converts first character of every word into uppercase.
#name=name.strip().capitalize().title()
#split() method will divide the input string into separate words & returns a list
#in python we can do multiple variable declaration&assignment in one line, but if there is no second value in the following case, it's an error.
print("total number of words in the name",len(name.split()))#finds the count of words in the user input.
#if(len(name.split()))
first,last=name.strip().capitalize().title().split()

#adding 'f' in the print statement directs the interpreter to format the statement & treat string included in {} as special.
#Means, it could be a variable, if so parse that variable and return its value.
print(f"hello {first} {last}")
#print(f"hello {third}") -> this is an error because interpreter tries to parse 'third' which is not defined in the code.git 