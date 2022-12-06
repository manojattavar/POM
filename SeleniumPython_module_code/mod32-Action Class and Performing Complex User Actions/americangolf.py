'''
Created on 05-May-2020
@author: jaspreet
'''
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import randint

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.americangolf.co.uk/")
e = driver.find_element_by_xpath("//*[@id='header-navigation']/div[1]/ul/li[3]/a")
webdriver.ActionChains(driver).move_to_element(e).perform()
wait= WebDriverWait(driver,10)
element = wait.until(EC.visibility_of_element_located((By.ID,"CLOTHFOOTW_1")))
links = element.find_elements_by_tag_name("a")
print("No. of links : "+str(len(links)))

l = links[randint(0,len(links))]
l.click()
# time.sleep(5)
# driver.quit()