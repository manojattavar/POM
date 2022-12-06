'''
Created on 09-May-2020
@author: jaspreet
'''
from selenium import webdriver
import subprocess

driver= webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://filebin.net/")
upload_button = driver.find_element_by_id("fileField")
webdriver.ActionChains(driver).click(upload_button).perform()
subprocess.Popen(["D:/eclipse/Modules/module21/upload.exe"])
