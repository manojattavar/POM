'''
Created on 24-Mar-2020
@author: jaspreet
'''
# import pytest
import logging
import sys
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

def test_try():
    with allure.step("Testing test case..."):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        l = logging.getLogger()
        l.setLevel(logging.INFO)
        l.info("This is logging info")
        l.critical("This is logging critical")
        l.error("This is logging error")
        allure.attach(driver.get_screenshot_as_png(),"Screenshot of eclipse", AttachmentType.PNG)
        print("This is stdout",file=sys.stdout)
        driver.quit()

# @pytest.fixture
# def smart():
#     global a,b
#     a= input("Enter variable 1 : ")
#     b= input("Enter variable 2 : ")  
#     yield 
#     print("- - - - - -  - - -- - -  -- ")  
#         
# @pytest.mark.run(order=1)
# def test_case_add(smart):
#     with allure.step("Testing test case..."):
#         driver = webdriver.Chrome()
#         l = logging.getLogger()
#         l.setLevel(logging.INFO)
#         l.info("This is logging info")
#         l.critical("This is logging critical")
#         l.error("This is logging error")
#         result = int(a) + int(b)
#         print("the Output is : "+str(result),file=sys.stdout)
#         allure.attach(driver.get_screenshot_as_png(),"Screenshot of eclipse", AttachmentType.PNG)
#         print("This is stdout",file=sys.stdout)
# #         print("this is stderr",file=sys.stderr)    
#     
# @pytest.mark.run(order=4)
# def test_case_difference(smart):
#     result = int(a) - int(b)
#     print("the Output is : "+str(result))
#     
# @pytest.mark.run(after="test_case_difference")
# def test_case_product(smart):
#     result = int(a) * int(b)
#     print("the Output is : "+str(result))
#     
# @pytest.mark.run(order=2)
# def test_case_div(smart):
#     result = int(a) / int(b)
#     print("the Output is : "+str(result))