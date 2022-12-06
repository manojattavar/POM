'''
Created on 08-May-2020
@author: jaspreet
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

name = "Jaspreet Kaur"
rowNumber=-1

def getRowNumByName(name):
    rows = driver.find_elements_by_xpath("//*[@id='dtBasicExample']/tbody/tr")
    for i in range(0, len(rows)):
        row = rows[i]
        cells = row.find_elements_by_tag_name("td")
        for j in range(0, len(cells)):
            if((cells[j].text)==name):
                return i+1      
    return -1

def isElementPresent(locator, locatorType):
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.presence_of_all_elements_located((locatorType, locator)))
        wait.until(EC.visibility_of_all_elements_located((locatorType, locator)))
    except Exception:
        return False
    return True
    
op = webdriver.ChromeOptions()
op.add_argument("--disable-notifications")
op.add_argument("--start-maximized")  
driver = webdriver.Chrome(options = op)
driver.implicitly_wait(10)
driver.get("https://mdbootstrap.com/docs/jquery/tables/pagination/")

page=1
rowNumber = getRowNumByName(name)
while(rowNumber==-1):
    if(isElementPresent("//*[@id='dtBasicExample_next']/a", "xpath")):
        driver.find_element_by_xpath("//*[@id='dtBasicExample_next']/a").click()
        page= page+1
        rowNumber=getRowNumByName(name)
    else:
        print("name not found")
        break
if(rowNumber!=-1):
    print("Page no. : "+str(page))
    print("Row no. : "+str(rowNumber))
    age = driver.find_element_by_xpath("//*[@id='dtBasicExample']/tbody/tr["+str(rowNumber)+"]/td[4]")
    print("age is : "+age.text)
else:
    print("code issue.....")


    
        

    



    
            