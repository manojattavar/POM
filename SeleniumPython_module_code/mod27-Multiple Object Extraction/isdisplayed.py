import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://news18.com")
driver.implicitly_wait(10)

# driver.find_element_by_xpath("//*[@id='mc_mainWrapper']/nav/div/div[2]/div[2]/ul/li[22]/a").click()
linklist = driver.find_elements_by_tag_name("a")
print(type(linklist))
print(len(linklist))

for i in range(0, len(linklist)):
    linktext = linklist[i].text
    print(linktext+" - "+str(linklist[i].is_displayed()))
    print(linktext + " - " + str(linklist[i].is_enabled()))

time.sleep(5)
driver.quit()