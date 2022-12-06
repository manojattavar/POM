import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://news18.com")
#dynamic waiting technique - implicit wait- global wait driver.find
driver.implicitly_wait(10)
homelink = driver.find_element_by_xpath("//*[@id='mc_mainWrapper']/nav/div/ul[2]/li[1]/a")
print(homelink.is_displayed())
print(homelink.is_enabled())
print("- - - - - - - - - - -")
indialink=driver.find_element_by_xpath("//*[@id='mc_mainWrapper']/nav/div/div[2]/div[2]/ul/li[4]/a")
print(indialink.is_displayed())
print(indialink.is_enabled())
time.sleep(5)
driver.quit()