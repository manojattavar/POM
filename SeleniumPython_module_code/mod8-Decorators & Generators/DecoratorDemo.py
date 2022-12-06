'''
Created on 16-Mar-2020
@author: jaspreet
'''
def smart_div(func):
    def inner(self,a,b):
        print("Dividing two numbers ",a, " and ",b)
        if(b==0):
            print("Division not possible")
            quit()
               
        return func(self,a,b)
    return inner            
   
class division:
    @smart_div
    def div(self,a,b):
        output=a/b
        return output
       
d = division()
print(d.div(56, 7))

