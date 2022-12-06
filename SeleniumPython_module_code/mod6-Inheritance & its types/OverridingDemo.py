'''
Created on 16-Mar-2020
@author: jaspreet
'''
class Employee:
    def emp_name(self,empName):
        self.empName = empName
        
    def emp_name(self,firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
class Employee_id(Employee):
    def emp_id(self, id):
        self.id = id
        
    def emp_name(self,empName):
        self.empName = empName 
        
    def show(self):
        print('{} : {} : '.format(self.empName, self.id, self.empName))
        
e= Employee_id()
e.emp_name("Jaspreet")
e.emp_id("0032")
e.show()
print("= = = = = = = = = = = = =  = = = =")
e.emp_name("Pankaj")
e.show()
print("= = = = = = = = = = = = =  = = = =")
e.emp_name("Varhsa")
e.show()
e.emp_name("jaspreet", "kaur")
