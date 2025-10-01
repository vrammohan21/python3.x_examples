#Open file
fileref=open("resources/demo.txt","r")#Write is not supported
#fileref=open("resources/demo.txt","a+")
#fileref=open("Python_outline.xlsx","r")
#fileref=open("testfile.txt","r")
print(f"fileref type={type(fileref)}")
#read whole file and store file contents
contents=fileref.readlines()
print(contents)
#fileref.write("I am in append mode100...")
""" for line in fileref:
    print(line.strip())
    contents=fileref.readlines()
    print(contents) """
#print(f"is my file closed? {fileref.close()}")
#print(contents)
#read the file line-by-line
#lines=fileref.readlines()
#for line in lines[13:21]:
#lines=fileref.readlines()
#print(f"Total lines in the file=",len(contents))

    #use for loop to print file contents
#Close file
fileref.close()