'''
Created on 07-May-2020
@author: jaspreet
'''
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://jqueryui.com/draggable/")
frames = driver.find_elements_by_tag_name("iframe")
print("No. of  frames are : "+str(len(frames)))

driver.switch_to.frame(0)
drag = driver.find_element_by_id("draggable")

print(drag.location['x'])
print(drag.location['y'])
print(" ")
webdriver.ActionChains(driver).drag_and_drop_by_offset(drag, 100, 50).perform()
print(drag.location['x'])
print(drag.location['y'])

# time.sleep(5)
# driver.quit()