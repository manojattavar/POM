'''
Created on 03-Jul-2020
@author: jaspreet
'''
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from _overlapped import NULL
import conftest
from testresources.applicationkeyword import applicationkeywords
from testresources.validatekeywords import validatekeywords
import logging
import time
from _datetime import datetime
from testresources import constants
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class genkeywords(applicationkeywords, validatekeywords):
    def __init__(self):
        self.prop = conftest.prop
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.driver = NULL
        
    def openBrowser(self, browsername):
        with allure.step("Opening browser - "+browsername):
            if(self.prop['GridRun']=='Y'):
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
                    self.driver = webdriver.Chrome(options=options)
                    self.driver.implicitly_wait(5)
                    self.driver.maximize_window()
                elif(browsername==constants.FIREFOX):
                    self.driver = webdriver.Firefox()
                elif(browsername==constants.EDGE):
                    self.driver = webdriver.Edge()
                else:
                    self.reportFailure("No browser specified")
            self.takeScreenshot()
        
    def navigate(self,url):
        with allure.step("Navigating to - "+self.prop[url]):
            Url = self.prop[url]
            self.driver.get(Url)
            self.takeScreenshot()
        
    def Click(self, locatorKey):
        with allure.step("Clicking on - "+locatorKey):
            self.getElement(locatorKey).click()
            self.takeScreenshot()
    
    def Type(self,locatorKey,data):
        with allure.step("Typing in - "+locatorKey+ " with data as - "+data):
            self.getElement(locatorKey).send_keys(data)
            self.takeScreenshot()
            
#common utility
    def waitForPageToBeLoaded(self):
        i=1
        while(i!=10):
            load_status = self.driver.execute_script("return document.readyState")
            if(load_status=='complete'):
                break
            else:
                time.sleep(2)
        
    def isElementPresent(self,locatorKey):
        wait = WebDriverWait(self.driver,20)
        elementList = []
        obj = self.prop[locatorKey]
        self.waitForPageToBeLoaded()
        if(locatorKey.endswith("_xpath")):
            elementList = wait.until(EC.presence_of_all_elements_located((By.XPATH, obj)))
        elif(locatorKey.endswith("_id")):
            elementList = wait.until(EC.presence_of_all_elements_located((By.ID, obj)))
        elif(locatorKey.endswith("_name")):
            elementList = wait.until(EC.presence_of_all_elements_located((By.NAME, obj)))
        else:
            elementList = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, obj)))
        
        if(len(elementList)==0):
            self.reportFailure("Element not present not webpage")
            return False

        else:
            return True
        
    def isElementVisible(self,locatorKey):
        wait = WebDriverWait(self.driver,20)
        elementList = []
        obj = self.prop[locatorKey]
        self.waitForPageToBeLoaded()
        if(locatorKey.endswith("_xpath")):
            elementList = wait.until(EC.visibility_of_all_elements_located((By.XPATH, obj)))
        elif(locatorKey.endswith("_id")):
            elementList = wait.until(EC.visibility_of_all_elements_located((By.ID, obj)))
        elif(locatorKey.endswith("_name")):
            elementList = wait.until(EC.visibility_of_all_elements_located((By.NAME, obj)))
        else:
            elementList = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, obj)))
        
        if(len(elementList)==0):
            self.reportFailure("Element not visible not webpage")
            return False
        else:
            return True
        
    def getElement(self,locatorKey):
        obj = self.prop[locatorKey]
        element = NULL
        if(self.isElementPresent(locatorKey) and self.isElementVisible(locatorKey)):
            try:
                if(locatorKey.endswith("_xpath")):
                    element=self.driver.find_element('xpath', obj)
                elif(locatorKey.endswith("_id")):
                    element=self.driver.find_element('id', obj)
                elif(locatorKey.endswith("_name")):
                    element=self.driver.find_element('name', obj)
                else:
                    element=self.driver.find_element('css_selector', obj)
                return element
            except Exception:
                self.reportFailure("Element not found")
        else:
            self.reportFailure("Element not present/visible on webpage : "+locatorKey)
            
    def Quit(self):
        if(self.driver!=NULL):
            self.driver.quit()

    def getRowNumByName(self,LeadName):
        self.waitForPageToBeLoaded()
        rows = self.driver.find_elements_by_xpath(self.prop["allLeadName_xpath"])
        for i in range(0, len(rows)):
            if((rows[i].text)==LeadName):
                return i+1
        return -1
    
    def ClickonLeadName(self,LeadName):
        with allure.step("Clicking on : "+LeadName):
            rNum = self.getRowNumByName(LeadName)
            el = self.driver.find_element_by_xpath(self.prop["LeadNamePart1_xpath"]+str(rNum)+self.prop["LeadNamePart2_xpath"])
            el.click()
            
    def DeleteLead(self):
        with allure.step("Accepting the alert...."):
            time.sleep(1)
            self.driver.find_element_by_xpath(self.prop["confirmDelete_xpath"])
            
    def SelectDate(self,date):
        with allure.step("Selecting the date...."):
            self.Click("closingDate_xpath")
            dt = datetime.strptime(date,"%d-%m-%Y")
            print(dt)
            year = dt.year
            month=dt.strftime("%B")
            day=dt.day
            desired_date = month+", "+str(year)
            print(desired_date)
            while True:
                displayed_date = self.driver.find_element_by_xpath("//*[@id='calenDiv']/div/div[1]/div/span[3]").text
                print(displayed_date)
                if(desired_date < displayed_date):
                    self.driver.find_element_by_id("nm").click()
                    self.driver.find_element_by_xpath("//td[text()="+str(day)+"]").click()
                    break
                elif(desired_date > displayed_date):
                    self.driver.find_element_by_id("pm").click()
                    self.driver.find_element_by_xpath("//td[text()="+str(day)+"]").click()
                    break
                