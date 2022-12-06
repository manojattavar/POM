'''
Created on 07-May-2020
@author: jaspreet
'''
name = "eClerx Services"
def getRowNumByName(name):
    rows = driver.find_elements_by_xpath("//table[@class='dataTable']/tbody/tr")
    for i in range(0,len(rows)):
        row = rows[i]
        cells = row.find_elements_by_tag_name("td")
        for j in range(0,len(cells)):
            cell = cells[j].text
            if(cell==name):
                return i+1
            
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://money.rediff.com/gainers")
rowNum= getRowNumByName(name)
print("Row num for "+name+ " is : "+str(rowNum))

currentPrice = driver.find_element_by_xpath("//table[@class='dataTable']/tbody/tr["+str(rowNum)+"]/td[4]")
print("Price is : "+currentPrice.text)

cells = driver.find_elements_by_xpath("//table[@class='dataTable']/tbody/tr["+str(rowNum)+"]/td")
for i in range(0, len(cells)):
    cellData = cells[i].text
    print(cellData)
    
time.sleep(5)
driver.quit()
    