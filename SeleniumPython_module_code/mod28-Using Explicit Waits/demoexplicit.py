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
driver.get("https://www.myntra.com/")
searchbox=driver.find_element_by_xpath("//*[@id='desktop-header-cnt']/div[2]/div[3]/input")
searchbox.click()
searchbox.send_keys("jeans")
if(elementPresent("xpath","//*[@id='desktop-header-cnt']/div[2]/div[3]/div/ul")):
    driver.find_element_by_xpath("//*[@id='desktop-header-cnt']/div[2]/div[3]/div/ul/li[4]").click()
else:
    print("Element not found")


time.sleep(5)
driver.quit()