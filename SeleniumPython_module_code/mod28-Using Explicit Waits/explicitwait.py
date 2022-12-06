import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def elementPresent(locatorType, locator):
    #present = true
    #not present = false
    wait = WebDriverWait(driver, 20)
    try:
        wait.until(EC.presence_of_element_located((locatorType, locator)))
        wait.until(EC.visibility_of_element_located((locatorType, locator)))
    except Exception:
        return False
    return True

driver = webdriver.Chrome()
driver.get("https://zoho.com")
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/a[4]").click()

if(elementPresent("id", "login_id")):
    driver.find_element_by_id("login_id").send_keys("hello")
else:
    print("Element not found")


time.sleep(5)
driver.quit()