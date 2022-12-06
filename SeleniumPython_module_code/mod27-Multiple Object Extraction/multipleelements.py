import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://news18.com")
driver.implicitly_wait(10)
#multiple elements
#return a list
linklist = driver.find_elements_by_tag_name("a")
print(type(linklist))
print(len(linklist))

for i in range(0, len(linklist)):
    linktext = linklist[i].text
    print(linktext)
time.sleep(5)
driver.quit()

# //*[@id="true"]/div[5]/div[2]/ul = sports
# //*[@id="true"]/div[5]/div[1]/ul = buzz