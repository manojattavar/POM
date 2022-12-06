import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://news18.com")
driver.implicitly_wait(10)
sportsblock = driver.find_element_by_xpath("//*[@id='true']/div[5]/div[2]/ul")  #unique elements
linklist = sportsblock.find_elements_by_tag_name("a")      #multiple elements
print(type(linklist))
print(len(linklist))

for i in range(0, len(linklist)):
    linktext = linklist[i].text
    print(linktext)


time.sleep(5)
driver.quit()