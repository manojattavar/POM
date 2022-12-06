'''
Created on 16-Mar-2020
@author: jaspreet
'''
from abc import ABC, abstractmethod
class HospitalA(ABC):
    @abstractmethod
    def OT(self):
        pass
    
    @abstractmethod
    def ortho(self):
        pass
    
    def ENT(self):
        print("I am in ENT fucntion")
    
    def OPD(self):
        print("I am in OPD fucntion")
        
class HospitalB(HospitalA):
    def OT(self):
        print("I am in OT Fucntion of Hospital B")
        
    def ortho(self):
        print("I am in ortho Fucntion of Hospital B")
        
    def Cardio(self):
        print("I am in Cardio Fucntion of Hospital B")
        

b= HospitalB()
b.ENT()
b.OT()
        
        