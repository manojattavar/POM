import subprocess
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})

chromePath = "C:\\Users\\029693744\\Desktop\\Selenium\\webdriver\\drivers\\chromedriver_win32\\chromedriver.exe"

driver = webdriver.Chrome(options=options, executable_path=chromePath)

driver.maximize_window()
driver.get("https://smallpdf.com/excel-to-pdf")
driver.find_element(By.XPATH, "//*[@id='__cond-28']/div/div/div/div/div/div/form/label/div/div[2]/div/button[1]/span").click()
time.sleep(2)

subprocess.Popen(["C:\\Users\\029693744\\Desktop\\Selenium\\autoit\\upload.exe"])
