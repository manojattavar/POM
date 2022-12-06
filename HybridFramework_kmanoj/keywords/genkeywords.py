import logging
import time

import _datetime as dt

import allure
from _overlapped import NULL
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from _datetime import datetime

from testResources import constants
import conftest


class genkeyword:

    def __init__(self):
        self.env = conftest.env
        self.prod = conftest.prod
        # self.driver = NULL

    def setObject(self, obj):
        self.obj = obj

    def setData(self, data):
        self.data = data

    def setTestData(self, testData):
        self.testData = testData

    def getBrowserOptions(self, browserName):
        if (browserName == constants.CHROME):
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            options.add_argument("--disable-notifications")
            return options
        elif (browserName == constants.FIREFOX):
            options = Options()
            options.set_preference("dom.webnotifications.enabled", True)
            return options

    def openbrowser(self):
        browserName = self.testData[self.data]
        if (browserName == constants.CHROME):
            options = self.getBrowserOptions(browserName)
            self.driver = webdriver.Chrome(options=options)
        elif (browserName == constants.FIREFOX):
            options = self.getBrowserOptions(browserName)
            self.driver = webdriver.Firefox(options=options)

    def navigate(self):
        URL = self.prod[self.obj]
        with allure.step("Navigating " + str(URL)):
            self.driver.get(URL)
            self.driver.maximize_window()

    def click(self, parameter=None):
        if (parameter == None):
            locatorKey = self.obj
            with allure.step("Clicking object -- " + str(locatorKey)):
                element = self.getElement(locatorKey)
                element.click()
        else:
            locatorKey = parameter
            with allure.step("Clicking object -- " + str(locatorKey)):
                element = self.getElement(locatorKey)
                element.click()

    def type(self, parameter=None, value=None):
        if (parameter == None and value == None):
            locatorKey = self.obj
            data = self.testData[self.data]
            with allure.step("Typing in object -- " + str(locatorKey) + " with data -- " + str(data)):
                element = self.getElement(locatorKey)
                if (element != NULL):
                    element.send_keys(data)
                else:
                    self.reportFailure("Element not found...")

        else:
            locatorKey = parameter
            if (value == 'Username' or value == 'Password'):
                data = self.env[value]
            else:
                data = self.testData[value]
            with allure.step("Typing in object -- " + str(locatorKey) + " with data -- " + str(data)):
                element = self.getElement(locatorKey)
                if (element != NULL):
                    element.send_keys(data)
                else:
                    self.reportFailure("Element not found...")


    def quit(self):
        try:
            self.driver.quit()
        except Exception as e:
            print("No active session found...")

    def refresh(self):
        self.driver.refresh()

    ############################ APPLICATION Specific functions ############################

    def doLogin(self):
        with allure.step("Performing Login steps..."):
            self.click('signin_xpath')
            self.type('email_id', 'Username')
            self.click('nextbutton_xpath')
            self.type('password_id', 'Password')
            self.click('nextbutton_xpath')

    def createLead(self):
        self.click('CRMLinkBtn_xpath')
        self.click('LeadsHomePageBtn_xpath')
        self.click('createLeadBtn_xpath')
        self.wait()
        self.type('companyName_xpath', constants.ACCOUNTNAME)
        self.type('firstName_xpath', constants.FIRSTNAME)
        self.type('lastName_xpath', constants.LASTNAME)
        self.wait()
        self.click('saveBtn_id')
        self.click('saveBackArrowBtn_id')
        self.refresh()
        rowNum = self.getRowNumberByName('nameList_xpath', self.testData[constants.FIRSTNAME] + ' ' + self.testData[constants.LASTNAME])

        if (rowNum == -1):
            self.reportFailure("Lead ID " + constants.FIRSTNAME + ' ' + constants.LASTNAME + " not present...")
        else:
            self.reportSuccess("Lead ID " + constants.FIRSTNAME + ' ' + constants.LASTNAME + " is present at the row number " + str(rowNum))


    def convertLead(self):
        self.click('CRMLinkBtn_xpath')
        self.click('LeadsHomePageBtn_xpath')
        rowNum = self.getRowNumberByName('nameList_xpath', self.testData[constants.LEADNAME])

        if (rowNum == -1):
            self.reportFailure("Lead ID " + constants.LEADNAME + " not present...")
        else:
            self.clickElementByRowNum(rowNum, 'namePart1_xpath', 'namePart2_xpath')
            self.wait()
            self.click('convertBtn_name')
            self.wait()
            self.click('convertBtnConfirmation_id')
            self.wait()
            self.click('goToLeadsButton_id')
            self.refresh()
            rowNum = self.getRowNumberByName('nameList_xpath', self.testData[constants.LEADNAME])

            if (rowNum == -1):
                self.reportSuccess("Lead ID " + constants.LEADNAME + " not present...")
            else:
                self.reportFailure("Lead ID " + constants.LEADNAME + " present and the row number is " + str(rowNum))

    def deleteLead(self):
        self.click('CRMLinkBtn_xpath')
        self.click('LeadsHomePageBtn_xpath')
        rowNum = self.getRowNumberByName('nameList_xpath', self.testData[constants.LEADNAME])

        if (rowNum == -1):
            self.reportFailure("Lead ID " + constants.LEADNAME + " not present...")
        else:
            self.clickElementByRowNum(rowNum, 'namePart1_xpath', 'namePart2_xpath')
            self.wait()
            self.click('deleteHomePageBtn_id')
            self.wait()
            self.click('deleteActualBtn_xpath')
            self.wait()
            self.click('deleteAlertButton_xpath')
            self.wait()
            rowNum = self.getRowNumberByName('nameList_xpath', self.testData[constants.LEADNAME])

            if (rowNum == -1):
                self.reportSuccess("Lead ID " + constants.LEADNAME + " not present...")
            else:
                self.reportFailure("Lead ID " + constants.LEADNAME + " present and the row number is " + str(rowNum))

    def createDeal(self):
        self.click('CRMLinkBtn_xpath')
        self.click('dealHomePageBtn_xpath')
        self.click('createDeal_xpath')
        self.wait()
        self.type('dealName_id', constants.DEALNAME)
        self.wait()
        self.click('dealAccountNameWindow_xpath')
        rowNum = self.getRowNumberByName('dealAccountNamesList_xpath', self.testData[constants.ACCOUNTNAME])
        self.wait()
        self.clickElementByRowNum(rowNum, 'accuntNamePart1_xpath', 'accuntNamePart2_xpath')
        self.wait()
        self.enterClosingDate(self.testData[constants.CLOSINGDATE])
        self.wait()
        self.click('saveBtn_id')
        self.click('saveBackArrowBtn_id')
        self.refresh()
        rowNum = self.getRowNumberByName('dealNameList_xpath', self.testData[constants.DEALNAME])

        if (rowNum == -1):
            self.reportFailure("Deal ID " + constants.DEALNAME + " not present...")
        else:
            self.reportSuccess("Deal ID " + constants.DEALNAME + " is present at the row number " + str(rowNum))



    def deleteDeal(self):
        self.click('CRMLinkBtn_xpath')
        self.click('dealHomePageBtn_xpath')
        self.wait()
        rowNum = self.getRowNumberByName('dealNameList_xpath', self.testData[constants.DEALNAME])

        if (rowNum == -1):
            self.reportFailure("Deal ID " + constants.DEALNAME + " not present...")
        else:
            self.clickElementByRowNum(rowNum, 'dealButtonXpath1_xpath', 'dealButtonXpath2_xpath')
            self.wait()
            self.click('deleteHomePageBtn_id')
            self.wait()
            self.click('deleteActualBtn_xpath')
            self.wait()
            self.click('deleteAlertButton_xpath')
            self.wait()
            rowNum = self.getRowNumberByName('dealNameList_xpath', self.testData[constants.DEALNAME])

            if (rowNum == -1):
                self.reportSuccess("Deal ID " + constants.DEALNAME + " not present...")
            else:
                self.reportFailure("Deal ID " + constants.DEALNAME + " present and the row number is " + str(rowNum))


    def validateTitle(self):
        with allure.step("Validating page title..."):
            expectedTitle = self.env[self.obj]
            actualTitle = self.driver.title
            if (expectedTitle == actualTitle):
                self.reportSuccess("Title validation success...")
            else:
                self.reportFailure("Title validation not success... ")

    def validateLogin(self):
        locatorKey = self.obj
        status = self.testData[self.data]

        element = self.getElement(locatorKey)

        if (element.is_displayed() and status == 'success'):
            self.reportSuccess("Login success...")
        else:
            self.reportFailure("Login not success...")


    ######################### Custom functions ######################

    def getRowNumberByName(self, locatorKey, userName):
        obj = self.env[locatorKey]

        if (self.isElementPresent(locatorKey) and self.isElementVisible(locatorKey)):

            if (locatorKey.endswith('xpath')):
                elements = self.driver.find_elements(By.XPATH, obj)
            elif (locatorKey.endswith('id')):
                elements = self.driver.find_elements(By.ID, obj)
            elif (locatorKey.endswith('name')):
                elements = self.driver.find_elements(By.NAME, obj)
            else:
                elements = self.driver.find_elements(By.CSS_SELECTOR, obj)

            for index in range(0, len(elements)):
                if (elements[index].text == userName):
                    return index+1
            return -1

    def clickElementByRowNum(self, rowNum, locatorKey1, locatorKey2):
        obj1 = self.env[locatorKey1]
        obj2 = self.env[locatorKey2]

        if (locatorKey1.endswith('xpath')):
            element = self.driver.find_element(By.XPATH, obj1 + str(rowNum) + obj2)
        elif (locatorKey1.endswith('id')):
            element = self.driver.find_element(By.ID, obj1 + str(rowNum) + obj2)
        elif (locatorKey1.endswith('name')):
            element = self.driver.find_element(By.NAME, obj1 + str(rowNum) + obj2)
        else:
            element = self.driver.find_element(By.CSS_SELECTOR, obj1 + str(rowNum) + obj2)

        element.click()

    def logging(self, message):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info(message)

    def takeScreenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "Screenshot at : " + str(datetime.now()), AttachmentType.PNG)

    def reportSuccess(self, message):
        self.logging(message)
        assert True, message

    def reportFailure(self, message):
        self.logging(message)
        self.takeScreenshot()
        assert False, message

    def wait(self):
        time.sleep(1)

    def WaitForPageToBeLoaded(self):
        i = 1
        while (i != 10):
            load_status = self.driver.execute_script("return document.readyState")
            if (load_status == 'complete'):
                break
            else:
                time.sleep(2)
                i += 1


    def isElementPresent(self, locatorKey):
        obj = self.env[locatorKey]

        self.WaitForPageToBeLoaded()

        wait = WebDriverWait(self.driver, 20)

        if (locatorKey.endswith('xpath')):
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, obj)))
        elif (locatorKey.endswith('id')):
            elements = wait.until(EC.presence_of_all_elements_located((By.ID, obj)))
        elif (locatorKey.endswith('name')):
            elements = wait.until(EC.presence_of_all_elements_located((By.NAME, obj)))
        else:
            elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, obj)))

        if (len(elements) != 0):
            return True
        else:
            return False

    def isElementVisible(self, locatorKey):
        obj = self.env[locatorKey]

        self.WaitForPageToBeLoaded()

        wait = WebDriverWait(self.driver, 20)

        if (locatorKey.endswith('xpath')):
            elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, obj)))
        elif (locatorKey.endswith('id')):
            elements = wait.until(EC.visibility_of_all_elements_located((By.ID, obj)))
        elif (locatorKey.endswith('name')):
            elements = wait.until(EC.visibility_of_all_elements_located((By.NAME, obj)))
        else:
            elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, obj)))

        if (len(elements) != 0):
            return True
        else:
            return False

    def getElement(self, locatorKey):

        obj = self.env[locatorKey]
        if (self.isElementPresent(locatorKey) and self.isElementVisible(locatorKey)):

            if (locatorKey.endswith('xpath')):
                element = self.driver.find_element(By.XPATH, obj)
            elif (locatorKey.endswith('id')):
                element = self.driver.find_element(By.ID, obj)
            elif (locatorKey.endswith('name')):
                element = self.driver.find_element(By.NAME, obj)
            else:
                element = self.driver.find_element(By.CSS_SELECTOR, obj)

            if (element != NULL):
                return element
            else:
                print("Element not found...")

    def enterClosingDate(self, closingDate):
        closingDate = '04-12-2022'
        formatted = dt.datetime.strptime(closingDate, '%d-%m-%Y')
        year = formatted.year
        month = formatted.month
        day = formatted.day

        formatted_month = formatted.strftime('%b')

        desiredDateMonthYear = str(formatted_month) + ' ' + str(day) + ', ' + str(year)
        desiredMonthYear = str(formatted.strftime('%B')) + ' ' + str(year)

        element = self.driver.find_element(By.XPATH, "//*[@id='Crm_Potentials_CLOSINGDATE_LInput']")
        time.sleep(1)
        element.send_keys(desiredDateMonthYear)
        time.sleep(1)

        month = self.driver.find_element(By.CSS_SELECTOR, "#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalMonthDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
        time.sleep(1)
        year = self.driver.find_element(By.CSS_SELECTOR, "#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalYearDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
        time.sleep(1)

        displayedMonthYear = str(month) + ' ' + str(year)

        while True:
            if (desiredMonthYear > displayedMonthYear):
                self.driver.find_element(By.XPATH,"//*[@id='lyteCalendar']/lyte-calendar/div/div/div[1]/div/span[1]").click()
                time.sleep(1)
                modifiedMonth = self.driver.find_element(By.CSS_SELECTOR, "#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalMonthDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
                time.sleep(1)
                modifiedyear = self.driver.find_element(By.CSS_SELECTOR,"#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalMonthDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
                time.sleep(1)
                modifiedMonthYear = str(modifiedMonth) + ' ' + str(modifiedyear)

                if (desiredMonthYear == modifiedMonthYear):
                    self.driver.find_element(By.XPATH, "//*[@id='Lyte_Calendar_Day_404']").click()
                    break

            elif (desiredMonthYear < displayedMonthYear):
                self.driver.find_element(By.XPATH, "//*[@id='lyteCalendar']/lyte-calendar/div/div/div[1]/div/span[6]").click()
                time.sleep(1)
                modifiedMonth = self.driver.find_element(By.CSS_SELECTOR, "#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalMonthDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
                time.sleep(1)
                modifiedyear = self.driver.find_element(By.CSS_SELECTOR,"#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalMonthDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
                time.sleep(1)
                modifiedMonthYear = str(modifiedMonth) + ' ' + str(modifiedyear)

                if (desiredMonthYear == modifiedMonthYear):
                    self.driver.find_element(By.XPATH, "//*[@id='Lyte_Calendar_Day_404']").click()
                    break
            else:
                break