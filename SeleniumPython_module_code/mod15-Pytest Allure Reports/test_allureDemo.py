'''
Created on 24-Mar-2020
@author: jaspreet
'''
import pytest
@pytest.fixture
def smart():
    global a,b
    a= input("Enter variable 1 : ")
    b= input("Enter variable 2 : ")  
    yield 
    print("- - - - - -  - - -- - -  -- ")  
    
@pytest.mark.run(order=1)
def test_case_add(smart):
    result = int(a) + int(b)
    print("the Output is : "+str(result))
    
@pytest.mark.run(order=4)
def test_case_difference(smart):
    result = int(a) - int(b)
    print("the Output is : "+str(result))
    
@pytest.mark.run(after="test_case_difference")
def test_case_product(smart):
    result = int(a) * int(b)
    print("the Output is : "+str(result))
    
@pytest.mark.run(order=2)
def test_case_div(smart):
    result = int(a) / int(b)
    print("the Output is : "+str(result))