import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://zoho.com")
#dynamic waiting technique - implicit wait- global wait driver.find
driver.implicitly_wait(10)
#gloBL WAIT
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/a[4]").click()
# time.sleep(5)       #pause
usernametextbox = driver.find_element_by_id("login_id")
usernametextbox.send_keys("seleniumtraining10@gmail.com")
print(usernametextbox.get_attribute("name"))
print(usernametextbox.get_attribute("value"))
#//*[@id="login_id"]


time.sleep(5)
driver.quit()