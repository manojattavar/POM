import time
from selenium import webdriver

fp = webdriver.FirefoxProfile("C:\\Users\\Abhishek\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dslne5iu.Jaspreet")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.dir", "D:\\Jaspreet\\temp")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.openxmlformats-officedocument.wordprocessingml.document, text/plain")

driver = webdriver.Firefox(fp)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.qtpselenium.com/downloads/download.html")
driver.find_element_by_link_text("xls download").click()

time.sleep(5)
driver.quit()
