#create a function
def demofunction():
    print("This is a demo function")

demofunction()

class DemoClass:
    a= 50
    def show(self):
        print(self.a)
        b=100
        print(b)

DemoClass().show()

class Student:
    #to initialize common variable
    #name, roll no, class, sub, sub teacher, class incharge, theory, practical, assessment
    def __init__(self, subject):
        self.subject = subject
        #default, paramterized
        # print("demo of default constructor)"

    def studentname(self,name):
        self.name = name

    def studentmarks(self, marks):
        self.marks = marks

    def show(self):
        print(self.name + " - "+self.subject+" - "+str(self.marks))

# Student().studentname("Ronn")
# Student().studentmarks(80)

s1 = Student("Mathematics")
s1.studentname("Ronn")
s1.studentmarks(80)
s1.show()

s2 = Student("Mathematics")
s2.studentname("Jerry")
s2.studentmarks(90)
s2.show()

s1 = s2
s1.show()