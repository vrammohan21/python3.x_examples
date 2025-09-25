#create a class called Student
class Student:
    __name__="John"
    id="4"
    grade='A'
    #self is the current object of the class & should be the first parameter.
    #self can be replaced with any other name as follows
    def __init__(self):
        self.__name__=__name__
        self.id=id
    def display1(self):
        print(self.id,self.__name__,self.grade)
    def display(student):
        print(student.id,student.grade,student.name)

#create an object of Student & invoke the method.
stu=Student()
stu.display1()
#stu.display()
print(f" ID={stu.id}, Name= {stu.__name__},")
print(f" ID={stu.id}, Name= {stu.__name__},")