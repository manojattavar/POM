'''
Created on 09-May-2020
@author: jaspreet
'''
from selenium import webdriver
driver= webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://filebin.net/")
upload_button = driver.find_element_by_id("fileField")
# webdriver.ActionChains(driver).click(upload_button).perform()
upload_button.send_keys("C:/Users/jaspreet/Desktop/flowers.jfif")
