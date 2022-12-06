from __future__ import division
from selenium import webdriver
import time
import datetime
from _datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from _decimal import Decimal
dynamicBrowsers= "Firefox"
  
 
 
def ClickandWait(xpathExpTarget , xpathExpWait , maxTime ):
    for i in range(0,maxTime):
        driver.find_element_by_xpath(xpathExpTarget).click()
           
        if(isElementPresent(xpathExpWait) and driver.find_element_by_xpath(xpathExpWait).is_displayed()):
            return
        else:
            time.sleep(1)
   
   
def isElementPresent(xpathExp):
    s=driver.find_elements_by_xpath(xpathExp)
       
    if(len(s) == 0):
        return False
    else:
        return True
       
    assert False
      
      
def deletePortfolio():
    driver.find_element_by_id("deletePortfolio").click()
    driver.switch_to_alert().accept()
    driver.switch_to.default_content()
     
    
    
def selectDate(d):
    CurrentDate=datetime.now() 
    print(CurrentDate.strftime('%d/%m/%Y'))
    dt=datetime.strptime(d,'%d/%m/%Y')
    Year=dt.year
    day=dt.day
    month=dt.strftime("%B")
    desiredMonthYear= str(month)+" "+str(Year)
    
    while True:
        displayedMonthYear=driver.find_element_by_css_selector(".dpTitleText").text
        if(desiredMonthYear==displayedMonthYear):
            driver.find_element_by_xpath("//td[text()= '"+str(day)+"']").click()
            break
        else:
            if(dt > CurrentDate):
                driver.find_element_by_xpath("//*[@id='datepicker']/table/tbody/tr[1]/td[4]/button").click()
            elif(dt < CurrentDate):
                driver.find_element_by_xpath("//*[@id='datepicker']/table/tbody/tr[1]/td[2]/button").click()
    
    
def getRowNumWithCellData(Data):
    Rows=driver.find_elements_by_xpath("//table[@id='stock']/tbody/tr")
    print(len(Rows))
    for i in range(0 , len(Rows)):
        Row=Rows[i] 
        Cells=Row.find_elements_by_tag_name("td")
          
        for j in range(0,len(Cells)):
            CellData=Cells[j].text
            print(CellData)
            print(Data)
              
              
            if(CellData.strip() != ("") and CellData==Data):
                return i
              
      
      
      
    return -1
          
def deleteStockTest():
    driver.find_element_by_xpath("//input[@name='Delete']").click()
    driver.switch_to.alert.accept()
    driver.switch_to.default_content()
     
     
     
def BuySellStock(a):
    driver.find_element_by_xpath("//input[@class='buySell']").click()
    driver.find_element_by_xpath("//*[@id='buySellCalendar']").click()
    driver.find_element_by_id("buysellqty").send_keys("100")
    driver.find_element_by_id("buysellprice").send_keys("400")
    driver.find_element_by_id("")
    CurrentDate=datetime.now() 
    print(CurrentDate.strftime('%d/%m/%Y'))
    dt=datetime.strptime(a,'%d/%m/%Y')
    Year=dt.year
    day=dt.day
    month=dt.strftime("%B")
    desiredMonthYear= str(month)+" "+str(Year)
     
    while True:
        displayedMonthYear=driver.find_element_by_css_selector(".dpTitleText").text
        if(desiredMonthYear==displayedMonthYear):
            driver.find_element_by_xpath("//td[text()= '"+str(day)+"']").click()
            break
        else:
            if(dt > CurrentDate):
                driver.find_element_by_xpath("//*[@id='datepicker']/table/tbody/tr[1]/td[4]/button").click()
            elif(dt < CurrentDate):
                driver.find_element_by_xpath("//*[@id='datepicker']/table/tbody/tr[1]/td[2]/button").click()
     
    
    
def TransactionHistory(): 
    driver.find_element_by_xpath("//table[@id='stock']/tbody/tr[1]/td[1]/input ").click()  
    driver.find_element_by_xpath("//input[@class='equityTransaction']").click() 
    shares=driver.find_elements_by_xpath("//table[@class='dataTable']/tbody/tr/td[3]")
    prices=driver.find_elements_by_xpath("//table[@class='dataTable']/tbody/tr/td[4]")
    
    totalShares=0
    totalAmount=0
    for i in range(0,len(prices)):
        share=shares[i].text
        print(share)
        price=prices[i].text
        print(price)
        totalShares=int(share) + totalShares
        totalAmount=totalAmount + (int(share)*int(price))
    
    print(totalShares)
    print(totalAmount)
    average= Decimal(totalAmount)/Decimal(totalShares)
    print(average)
    
    
    
    
webdriver.driver= None
    
if dynamicBrowsers == "Firefox":
    driver=webdriver.Firefox()
        
      
elif dynamicBrowsers == "Chrome":
    driver=webdriver.Chrome()
         
         
elif dynamicBrowsers == "Ie":
    driver = webdriver.Ie()
     
elif dynamicBrowsers == "Edge":
    driver = webdriver.Edge()
    
    
driver.implicitly_wait(5)  
driver.maximize_window()
driver.get("https://www.rediff.com/")
driver.find_element_by_xpath("//*[@id='homewrapper']/div[5]/a[3]/div/u").click()
driver.find_element_by_xpath("//*[@id='signin_info']/a[1]").click()
driver.find_element_by_id("useremail").send_keys("abhiguleria143@gmail.com")
driver.find_element_by_id("emailsubmit").click()
wait=WebDriverWait(driver, 10)
element=wait.until(EC.visibility_of_element_located((By.ID , "userpass")))
driver.find_element_by_id("userpass").send_keys("Abhijeet@35")
driver.find_element_by_id("userpass").send_keys(Keys.ENTER)
ClickandWait(xpathExpTarget = "//*[@id='createPortfolio']/img" , xpathExpWait = "//*[@id='createPortfolioButton']" , maxTime = 10)        
driver.find_element_by_id("create").clear()
driver.find_element_by_id("create").send_keys("qkghgfn")
driver.find_element_by_id("createPortfolioButton").click()
e=driver.find_element_by_id("portfolioid")
select=Select(e)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, 'addStock')))
driver.find_element_by_id("addStock").click()
driver.find_element_by_id("addstockname").send_keys("tata")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//div[@id='ajax_listOfOptions']/div[2]").click()
driver.find_element_by_id("addstockqty").send_keys("100")
driver.find_element_by_id("addstockprice").send_keys("500")
driver.find_element_by_id("stockPurchaseDate").click()
selectDate("15/02/2018") 
driver.find_element_by_id("addStockButton").click()
driver.set_page_load_timeout(10)
time.sleep(5)
i=getRowNumWithCellData("Tata Steel")
print(i)
b= driver.find_element_by_xpath("//table[@id='stock']/tbody/tr[1]/td[1]/input ").click()
BuySellStock("12/02/2018")
driver.find_element_by_id("buySellStockButton").click()
time.sleep(5)
TransactionHistory()


                        
                         


    
    

