file1='./testfile.txt'

def talk2file(file1,content,mode):
    with open(file1,mode) as wf:
        wf.write(content)#If mode='w' , content will be overwritten. if the mode='a+' content will be appended. NO DATA LOSS.

def readfromfile(file1):
        with open(file1,'r') as rf:
            #print(rf.mode)
            print(rf.read())


talk2file(file1,"\nI was appended",'a+')
readfromfile(file1)