'''
Created on 07-May-2020
@author: jaspreet
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://money.rediff.com/gainers")

rows = driver.find_elements_by_xpath("//table[@class='dataTable']/tbody/tr")
print("No. of rows : "+str(len(rows)))

columns = driver.find_elements_by_xpath("//table[@class='dataTable']/tbody/tr[1]/td")
print("No. of columns : "+str(len(columns)))

companyNames = driver.find_elements_by_xpath("//table[@class='dataTable']/tbody/tr/td[1]")
currentPrice = driver.find_elements_by_xpath("//table[@class='dataTable']/tbody/tr/td[4]")

companyName = "TCI Developers Ltd."
for i in range(0, len(companyNames)):
    name = companyNames[i].text
    price = currentPrice[i].text
    print(name+" --- "+price)
    if(name==companyName):
        print("Price is : "+price)
        break
    
time.sleep(5)
driver.quit()