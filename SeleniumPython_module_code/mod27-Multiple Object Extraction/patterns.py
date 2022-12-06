import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://news18.com")
driver.implicitly_wait(10)

part1 = "//*[@id='true']/div[3]/div[2]/ul/li["
part2 = "]/a"

for i in range(1,8):
    link = driver.find_element_by_xpath(part1+str(i)+part2)
            #//*[@id='true']/div[3]/div[2]/ul/li[]/a[2]
    linktext = link.text
    print(linktext)
time.sleep(5)
driver.quit()