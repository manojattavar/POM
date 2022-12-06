'''
Created on 16-Mar-2020
@author: jaspreet
'''
class Operation:
    def __init__(self):
        self.a = 80             #Default public variables
        self.b = 59
        self._c = 10            #Protected Variable
        self._d = 20    
        self.__e = 63           #Private Variable
        self.__f = 85
        
    def add(self):
        total = self.a + self.b
        print("The total is : "+str(total)+" with public variables")
    
    def add_p(self):
        total = self._c + self._d
        print("The total is : "+str(total)+" with protected variables")
        
    def add_pp(self):
        total = self.__e + self.__f
        return total
#         print("The total is : "+str(total)+" with private variables")
        
class output:
    o=Operation()
    def __sum_pp(self):
        return self.o.add_pp()
    
    def total(self):
        return self.__sum_pp()
    
    
o=output()
print(o.total())
        
        
    
    
        
# o=Operation()
# o.add()
# o.add_p()
# o.add_pp()