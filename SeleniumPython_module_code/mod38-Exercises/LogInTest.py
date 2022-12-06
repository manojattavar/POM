'''
Created on 20-Feb-2019

@author: Riya
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
dynamicBrowsers= "Chrome"
 
webdriver.driver= None
 
if dynamicBrowsers == "Firefox":
    driver=webdriver.Firefox()
#     driver.get("https://www.google.com/")
     
   
elif dynamicBrowsers == "Chrome":
    driver=webdriver.Chrome()
#     driver.get("https://www.google.com/")
     
     
elif dynamicBrowsers == "Ie":
    driver = webdriver.Ie()
#     driver.get("https://www.google.com/")
 
elif dynamicBrowsers == "Edge":
    driver = webdriver.Edge()


driver.implicitly_wait(5)
# driver.set_page_load_timeout(5)   
driver.maximize_window()
driver.get("https://www.rediff.com/")
driver.find_element_by_xpath("//*[@id='homewrapper']/div[5]/a[3]/div/u").click()
driver.find_element_by_xpath("//*[@id='signin_info']/a[1]").click()
driver.find_element_by_id("useremail").send_keys("abhiguleria143@gmail.com")
driver.find_element_by_id("emailsubmit").click()
wait=WebDriverWait(driver, 10)
element=wait.until(EC.visibility_of_element_located((By.ID , "userpass")))
driver.find_element_by_id("userpass").send_keys("Abhijeet@35")
driver.find_element_by_id("userpass").send_keys(Keys.ENTER)
# driver.find_element_by_id("loginsubmit").click()

