from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element_by_id("login1").send_keys("hello")
wait = WebDriverWait(driver, 10)
proceedBtn = wait.until(EC.presence_of_element_located((By.NAME, "proceed")))
proceedBtn.click()

a = wait.until(EC.alert_is_present())
print(a.text)
# a.accept()
a.dismiss()