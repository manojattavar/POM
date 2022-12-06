import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://edition.cnn.com/")
cookies = driver.get_cookies()
cookie=iter(cookies)
for i in cookie:
    pass
    # print(i['name']+" --- "+i['value'])
    # if(i['name']=="stateCode"):
        # driver.delete_cookie("stateCode")
        # cookies = driver.get_cookies()
        # cookie = iter(cookies)
        # print(" ")
        # for i in cookie:
        #     print(i['name'] + " --- " + i['value'])

new_cookie = {'name':'new', 'value':'cookie'}
driver.add_cookie(new_cookie)
cookies = driver.get_cookies()
cookie=iter(cookies)
for i in cookie:
    print(i['name']+" --- "+i['value'])

driver.delete_all_cookies()

time.sleep(5)
driver.quit()