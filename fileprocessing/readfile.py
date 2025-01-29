#Open file
fileref=open("learnpython.txt","r")
#fileref=open("Python_outline.xlsx","r")
#fileref=open("testfile.txt","r")
#print(f"fileref type={type(fileref)}")
#read whole file and store file contents
contents=fileref.read()
#print(contents)
#read the file line-by-line
#lines=fileref.readlines()
#for line in lines[13:21]:
#lines=fileref.readlines()
print(f"Total lines in the file=",len(contents))
for line in fileref:
    print(line.strip())
    #use for loop to print file contents
#Close file
fileref.close()