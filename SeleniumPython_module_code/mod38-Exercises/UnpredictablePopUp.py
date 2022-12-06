'''
Created on 12-Mar-2019

@author: Riya
'''

from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://qtpselenium.com/test/unpredictable.php")
handles=set(driver.window_handles)
size=len(handles)
print(size)
if (size==2):
    my_iter=iter(handles)
    mainWindowId=next(my_iter)
    popUpId=next(my_iter)
    driver.switch_to.window(popUpId)
    driver.close()
    driver.switch_to.window(mainWindowId)