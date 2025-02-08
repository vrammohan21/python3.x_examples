#create a class called Student
class Student:
    name="John"
    id="4"
    grade='A'
    #self is the current object of the class & should be the first parameter.
    #self can be replaced with any other name as follows
    '''def display(self):
        print(self.id,self.name,self.grade)'''
    def display(student):
        print(student.id,student.grade,student.name)

#create an object of Student & invoke the method.
stu=Student()
stu.display()