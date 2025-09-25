#print(3+2*2)
#print(int(3.2))
A='1234567'
#print(A[1::2])
""" Name="Michael Jackson"
print(Name.find('el'))
 """
""" t1=((11,12),[21,22])
print(t1[0][1]) """

""" V={'A','B'}
V.add('C')
print(V)
 """



""" x="Go"

if(x!="Go"):

    print('Stop')

else:

    print('Go ')

print('Mike') """
""" 

x="Go"

if(x=="Go"):

    print('Go ')

else:

    print('Stop')

print('Mike')
 """


""" A=['1','2','3']

for a in A:

    print(2*a) """


""" def Add(x,y):

    z=y+x

    return(y)

print(Add('1','1')) """


class Points(object):

    def __init__(self,x,y):

        self.x=x
        self.y=y

    def print_point(self):

        print('x=',self.x,'y=',self.y)

p=Points(2,4)
#print(p.__dict__)
p.print_point()