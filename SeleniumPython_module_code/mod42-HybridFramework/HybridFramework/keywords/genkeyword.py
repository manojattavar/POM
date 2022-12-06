'''
Created on 24-Jul-2020
@author: jaspreet
'''
import conftest
from _overlapped import NULL
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import allure
from allure_commons.types import AttachmentType
import logging
from _datetime import datetime
from testResources import constants
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class genKeywords:
    def __init__(self):
        self.prod = conftest.prod
        self.envProp = conftest.envProp
        self.driver = NULL
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        
    def set_ObjectKey(self, OK):
        self.objectKey = OK
        
    def set_dataKey(self, DK):
        self.dataKey = DK
        
    def set_data(self, testData):
        self.data = testData
        
    def openBrowser(self):
        browsername = self.data[self.dataKey]
        #gridRun - y - another actions
        #n - 
        if(self.envProp['GridRun']==constants.Y):
            if(browsername==constants.CHROME):
                caps = DesiredCapabilities.CHROME.copy()
                caps['browserName']='chrome'
                caps['javascriptEnabled']=True
            elif(browsername==constants.FIREFOX):
                caps = DesiredCapabilities.FIREFOX.copy()
                caps['browserName']='firefox'
                caps['javascriptEnabled']=True
            try:
                self.driver = webdriver.Remote(desired_capabilities=caps, command_executor='http://192.168.42.208:4444/wd/hub')
            except Exception as e:
                print(e)
        else:
            if(browsername==constants.CHROME):
                options = webdriver.ChromeOptions()
                options.add_argument("--disable-infobars")
                options.add_argument("--disable-notifications")
                options.add_argument("--start-maximized")
                self.driver = webdriver.Chrome(options=options)
            elif(browsername==constants.FIREFOX):
                self.driver = webdriver.Firefox()
        self.takeScreenshot()
            
    def navigate(self):
        url = self.envProp[self.objectKey]
        with allure.step("Navigating to - "+url):
            self.driver.get(url)
            self.takeScreenshot()
        
    def click(self, parameter=None):
        if(parameter==None):
            with allure.step("Clicking on - "+self.objectKey):
                if(self.getElement(self.objectKey)):
                    self.getElement(self.objectKey).click()
                    self.takeScreenshot()
                else:
                    self.reportFailure("Element to be clicked "+self.objectKey+" not found")
        else:
            with allure.step("Clicking on - "+parameter):
                if(self.getElement(parameter)):
                    self.getElement(parameter).click()
                    self.takeScreenshot()
                else:
                    self.reportFailure("Element to be clicked "+parameter+" not found")
        
    def typing(self):
        with allure.step("Typing in - "+self.objectKey+" with - "+self.data[self.dataKey]):
            self.getElement(self.objectKey).send_keys(self.data[self.dataKey])
            self.takeScreenshot()
            
    def type(self, arg1, arg2):
        with allure.step("Typing in - "+arg1+" with - "+arg2):
            self.getElement(arg1).send_keys(arg2)
            self.takeScreenshot()
        
    #common utility functions
    def waitForPageToBeLoaded(self):
        i=1
        while(i!=10):
            load_status = self.driver.execute_script("return document.readyState")
            if(load_status=='complete'):
                break
            else:
                time.sleep(2)
                
    def isElementPresent(self, locator):
        wait = WebDriverWait(self.driver, 20)
        elementList = []
        obj = self.prod[locator]
        self.waitForPageToBeLoaded()
        if(locator.endswith('_xpath')):
            elementList = wait.until(EC.presence_of_all_elements_located((By.XPATH,obj)))
        elif(locator.endswith('_id')):
            elementList = wait.until(EC.presence_of_all_elements_located((By.ID,obj)))
        elif(locator.endswith('_name')):
            elementList = wait.until(EC.presence_of_all_elements_located((By.NAME,obj)))
        elif(locator.endswith('_cssSelector')):
            elementList = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,obj)))
        else:
            elementList = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,obj)))
                
        if(len(elementList)==0):
            return False
        else:
            return True
        
    def isElementVisible(self,locator):
        wait = WebDriverWait(self.driver, 20)
        elementList = []
        obj = self.prod[locator]
        self.waitForPageToBeLoaded()
        if(locator.endswith('_xpath')):
            elementList = wait.until(EC.visibility_of_all_elements_located((By.XPATH,obj)))
        elif(locator.endswith('_id')):
            elementList = wait.until(EC.visibility_of_all_elements_located((By.ID,obj)))
        elif(locator.endswith('_name')):
            elementList = wait.until(EC.visibility_of_all_elements_located((By.NAME,obj)))
        elif(locator.endswith('_cssSelector')):
            elementList = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,obj)))
        else:
            elementList = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME,obj)))
            
        if(len(elementList)==0):
            return False
        else:
            return True
        
    def getElement(self, locator):
        obj = self.prod[locator]
        element = NULL
        if(self.isElementPresent(locator) and self.isElementVisible(locator)):
            try:
                if(locator.endswith('_xpath')):
                    element = self.driver.find_element_by_xpath(obj)
                elif(locator.endswith('_id')):
                    element = self.driver.find_element_by_id(obj)
                elif(locator.endswith('_name')):
                    element = self.driver.find_element_by_name(obj)
                elif(locator.endswith('_cssSelector')):
                    element = self.driver.find_element_by_css_selector(obj)
                elif(locator.endswith('_className')):
                    element = self.driver.find_element_by_class_name(obj)
                else:
                    return False
                return element
            except Exception:
                self.reportFailure("The element -"+locator+" not found")
        else:
            self.reportFailure("The element -"+locator+" not present/ visible")
        
    def quit(self):
        if(self.driver!=NULL):
            self.driver.quit()
            
    def takeScreenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(),"Screenshot taken at : "+str(datetime.now()),AttachmentType.PNG)
        
    def reportFailure(self,message):
        self.takeScreenshot()
        assert False, message
        
    def reportSuccess(self,message):
        self.takeScreenshot()
        self.logging(message)
        assert True
        
    def logging(self, message):
        self.logger.info(message)
        
    def wait(self):
        time.sleep(5)
        
    def selectDate(self):
        with allure.step("Selecting date : "+self.data['ClosingDate']):
            date = self.data['ClosingDate']
            dt = datetime.strptime(date,"%d-%m-%Y")
            year = dt.year
            month=dt.strftime("%B")
            day=dt.day
            desired_date = month+" "+str(year)
            while True:
                displayed_date = self.driver.find_element_by_xpath("//*[@id='calenDiv']/div/div[1]/div/span[3]").text
                if(desired_date > displayed_date):
                    self.driver.find_element_by_id("nm").click()
                    self.driver.find_element_by_xpath("//td[text()="+str(day)+"]").click()
                    break
                elif(desired_date < displayed_date):
                    self.driver.find_element_by_id("pm").click()
                    self.driver.find_element_by_xpath("//td[text()="+str(day)+"]").click()
                    break
    
    def validateTitle(self):
        with allure.step("Validating URL Title..."):
            expectedTitle = self.prod[self.objectKey]
            actualTitle = self.driver.title
            if(expectedTitle==actualTitle):
                self.reportSuccess("Title Validation successful")
            else:
                self.reportFailure("Title Validation Failed...Got title as "+actualTitle+" instead of "+expectedTitle)
                
    def validateLogin(self):
        with allure.step("Validating login...."):
            element = self.getElement(self.objectKey)
            if(element.is_displayed() and self.data[self.dataKey]=='Success'):
                self.reportSuccess("Login Successful")
            else:
                self.reportFailure("Login Failed")
    
    def getRowCount(self,name):
        with allure.step("Checking lead....."):
            rows = self.driver.find_elements_by_xpath(self.prod['allLeads_xpath'])
            for i in range(0, len(rows)):
                if((rows[i].text)==name):
                    return i+1
            return -1
        
    def clickLeadName(self,name):
        rnum = self.getRowCount(name)
        element = self.driver.find_element_by_xpath(self.prod['LeadNamePart1_xpath']+str(rnum)+self.prod['LeadNamePart2_xpath'])
        element.click()
        
    def acceptingAlert(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        a = self.driver.switch_to.alert
        print(a.text)
        a.accept()
        self.driver.switch_to.default_content()
                
    def doLogin(self):
        with allure.step("Log In..."):
            self.click("loginLink_xpath")
            self.type("usernameTextBox_id", self.envProp['defaultUsername'])
            self.click("submitEmailBtn_xpath")
            self.type("passwordTextBox_name", self.envProp['defaultPassword'])
            self.click("signInBtn_xpath")
            
    def createLead(self):
        with allure.step("Creating Lead..."):
            self.click("crmlink_xpath")  
            self.click("leadbtn_xpath")
            self.click("addbtn_xpath")
            self.type("companynametextBox_id", self.data['CompanyName'])
            self.type("firstnametextBox_id", self.data['FirstName'])
            self.type("lastnametextBox_id", self.data['LastName'])
            self.click("saveleadbtn_id")
            self.click("backBtn_xpath")
            self.wait()
            self.getRowCount(self.data['LeadName'])
            
    def convertLead(self):
        with allure.step("Converting Lead.."+self.data['LeadName']):
            self.click("crmlink_xpath")  
            self.click("leadbtn_xpath")
            self.wait()
            rNum = self.getRowCount(self.data['LeadName'])
            if(rNum==-1):
                self.reportFailure("LeadName "+self.data['LeadName']+" does not exist in lead list")
            else:
                self.clickLeadName()    
                self.click("convertBtn_xpath")
                self.click("saveConvertLeadbtn_xpath")
                self.click("gotoleadsBtn_name")
                rNum = self.getRowCount(self.data['LeadName'])
                if(rNum==-1):
                    self.reportSuccess("LeadName "+self.data['LeadName']+" converted, does not exist in lead list")
                else:
                    self.reportFailure("LeadName "+self.data['LeadName']+" not converted, exist in lead list")
                    
    def deleteLead(self):
        with allure.step("Deleting lead....."):
            self.click("crmlink_xpath")
            self.click("contactLink_xpath")
            self.wait()
            rNum = self.getRowCount(self.data['LeadName'])
            if(rNum==-1):
                self.reportFailure("LeadName "+self.data['LeadName']+" not available in the list")
            else:
                self.clickLeadName()
                self.click("options_id")
                self.click("deletebtn_xpath")
                self.click("confirmDelete_xpath")
                rNum = self.getRowCount(self.data['LeadName'])
                if(rNum==-1):
                    self.reportSuccess("LeadName "+self.data['LeadName']+" deleted successfully")
                else:
                    self.reportFailure("LeadName "+self.data['LeadName']+" not deleted")
                    
    def createDeal(self):
        with allure.step("Creating Deal..."):
            self.click("crmlink_xpath")
            self.click("optionsTab_xpath")  
            self.click("dealLink_xpath")
            self.click("addbtn_xpath")
            self.type("DealNametxtBox_xpath", self.data['DealName'])
            self.type("accounttxtBox_xpath", self.data['Account'])
            self.type("stage_xpath", self.data['Stage'])
            self.click("closingDate_xpath")
            self.selectDate()
            self.click("saveDealbtn_xpath")
            self.click("backBtn_xpath")
            self.wait()
            rNum = self.getRowCount(self.data['DealName'])
            if(rNum==-1):
                self.reportFailure("DealName "+self.data['DealName']+" not found")
            else:
                self.reportSuccess("DealName "+self.data['DealName']+" found at row no. : "+str(rNum))
                
    def deleteDeal(self):
        with allure.step("Deleting Deal....."):
            self.click("crmlink_xpath")
            self.click("optionsTab_xpath")
            self.click("dealLink_xpath")
            self.wait()
            rNum = self.getRowCount(self.data['DealName'])
            if(rNum==-1):
                self.reportFailure("DealName "+self.data['DealName']+" not available in the list")
            else:
                self.clickLeadName(self.data['DealName'])
                self.click("options_id")
                self.click("deletedeal_xpath")
                self.click("confirmDelete_xpath")
                rNum = self.getRowCount(self.data['DealName'])
                if(rNum==-1):
                    self.reportSuccess("DealName "+self.data['DealName']+" deleted successfully")
                else:
                    self.reportFailure("DealName "+self.data['DealName']+" not deleted")                