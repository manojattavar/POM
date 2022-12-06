'''
Created on 16-Mar-2020
@author: jaspreet
'''

class Employee:
    def emp_name(self,empName):
        self.empName = empName
        
class Employee_id(Employee):
    def emp_id(self, id):
        self.id = id
        
    def show(self):
        print('{} : {}'.format(self.empName, self.id))
        
        
i= Employee_id()
i.emp_name("Jaspreet")
i.emp_id("0032")
i.show()