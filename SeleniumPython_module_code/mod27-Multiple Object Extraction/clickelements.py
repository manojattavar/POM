import time
from selenium import webdriver

def elementPresent(locatorType, locator):
    #present = true
    #not present = false
    element = []
    if(locatorType=='xpath'):
        element = driver.find_elements_by_xpath(locator)
    elif(locatorType=='cssSelector'):
        element = driver.find_elements_by_css_selector(locator)
    elif (locatorType == 'id'):
        element = driver.find_elements_by_id(locator)
    elif (locatorType == 'name'):
        element = driver.find_elements_by_name(locator)
    elif (locatorType == 'className'):
        element = driver.find_elements_by_className(locator)
    else:
        element = driver.find_elements_by_tagName(locator)

    if(len(element)==0):
        return False
    else:
        return True

driver = webdriver.Chrome()
driver.get("https://news18.com")
driver.implicitly_wait(10)
# maintab = driver.find_element_by_xpath("//*[@id='mc_mainWrapper']/nav/div/ul[2]")  #unique elements
# linklist = maintab.find_elements_by_tag_name("a")      #multiple elements
# print(type(linklist))
# print(len(linklist))

part1 = "//*[@id='mc_mainWrapper']/nav/div/ul[2]/li["
part2 = "]/a"

i=2
while(elementPresent("xpath", part1 + str(i) + part2)):
    link = driver.find_element_by_xpath(part1 + str(i) + part2)
    linktext = link.text
    print(linktext)
    link.click()
    print(driver.title)
    time.sleep(5)
    driver.back()
    i=i+1
else:
    print("No more elements found")

time.sleep(5)
driver.quit()