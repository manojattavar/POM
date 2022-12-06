'''
Created on 18-May-2020
@author: jaspreet
'''
from selenium import webdriver
browserName = "firefox"
if(browserName=='chrome'):
    driver = webdriver.Chrome()
elif(browserName=='firefox'):
    driver = webdriver.Firefox()
elif(browserName=='ie'):
    driver = webdriver.Ie()
elif(browserName=='edge'):
    driver = webdriver.Edge()
else:
    print("no browser specified")

driver.maximize_window()
driver.get("https://www.facebook.com/")

# textbox = driver.find_element_by_name("firstname")
# textbox.send_keys("hello")
#  
# emailtextbox = driver.find_element_by_id("email")
# emailtextbox.send_keys("hello")

# firstname = driver.find_element("name", "firstname")
# firstname.send_keys("hello")

driver.find_element("name", "firstname").send_keys("hello")


