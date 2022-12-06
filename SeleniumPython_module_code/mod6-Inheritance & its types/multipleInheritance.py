'''
Created on 16-Mar-2020
@author: jaspreet
'''
class Employee_id:
    def emp_id(self, id):
        self.id = id
        
class Employee_DOB:
    def emp_dob(self,dob):
        self.dob = dob
        
class Employee(Employee_DOB, Employee_id):
    def emp_name(self,empName):
        self.empName = empName
        
    def show(self):
        print('{} : {} : {}'.format(self.empName, self.id, self.dob))    

d= Employee()
d.emp_name("Jaspreet")
d.emp_id("0032")
d.emp_dob("25/02/1998") 
d.show() 