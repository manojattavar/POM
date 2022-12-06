'''
Created on 19-May-2020
@author: jaspreet
'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
# completeXPATH = driver.find_element_by_xpath("html/body/div/div[3]/div/div/div/div/div/div/div/div")
# print(completeXPATH.text)

# partialXpath = driver.find_element_by_xpath("//*[@id='email']")
# partialXpath.send_keys("uwrtpov")
# driver.find_element_by_class_name("._2zrpKA._1dBPDZ").send_keys("123")

driver.find_element_by_css_selector("form[autocomplete=on] > div:nth-child(1) > input").send_keys("123")

