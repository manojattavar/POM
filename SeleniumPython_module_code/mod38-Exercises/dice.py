'''
Created on 12-Mar-2019

@author: Riya
'''
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.dice.com/")
driver.find_element_by_name('q').send_keys("Selenium")
options=driver.find_elements_by_xpath("//ul[@class='typeahead__list']/li")
print(len(options))
for i in options:
    print(i.text)
    if(i.text=="Selenium WebDriver"):
        i.click()
        break
driver.find_element_by_id("search-field-location").clear()    
driver.find_element_by_id("search-field-location").send_keys("New York")
time.sleep(3)
options=driver.find_elements_by_xpath("//ul[@class='typeahead dropdown-menu']/li")
print(len(options))
for j in options:
    print(j.text)
    if(j.text=="New York, NY"):
        j.click()
        
        
driver.find_element_by_id("findTechJobs").click()
i=1
while i<=5:
    print(i)
    
    jobLinks=driver.find_elements_by_xpath("//ul[@class='list-inline']/li/h3/a/span")
    for k in jobLinks:
        if(k.text.strip() != ("")):
            print(k.text)
        
    i=i+1
    if(i==6):
        break
    driver.find_element_by_xpath("//*[@id='resultSec']/div[1]/div[6]/div[2]/div/ul/li/a").click()
