import logging
import time

from _overlapped import NULL
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait

import conftest
from testresources import Constants
from selenium import webdriver
from allure_commons.types import AttachmentType
import _datetime as dt
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from _datetime import datetime
import allure


class BasePage:
    def __init__(self):
        self.prop = conftest.prop

    def getBrowserOptions(self, browserName):
        if (browserName == Constants.CHROME):
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            options.add_argument("--disable-notifications")
            return options
        elif (browserName == Constants.FIREFOX):
            options = Options()
            options.set_preference("dom.webnotifications.enabled", True)
            return options


    def openbrowser(self, browserName):
        if (browserName == Constants.CHROME):
            options = self.getBrowserOptions(browserName)
            self.driver = webdriver.Chrome(options=options)
            return self.driver
        elif (browserName == Constants.FIREFOX):
            options = self.getBrowserOptions(browserName)
            self.driver = webdriver.Firefox(options=options)
            return self.driver

    def navigate(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def click(self, locatorKey):
        element = self.getElement(locatorKey)
        element.click()

    def type(self, locatorKey, data):
        element = self.getElement(locatorKey)
        element.send_keys(data)

    def wait(self):
        time.sleep(1)

    def refresh(self):
        self.driver.refresh()

    def quit(self):
        try:
            self.driver.quit()
        except Exception as e:
            print("No active session found...")

    def validateLogin(self, locatorKey, expResult):
        element = self.getElement(locatorKey)
        if (element.is_displayed() and expResult == 'success'):
            self.reportSuccess("Login validation success...")
        else:
            self.reportFailure("Login validation not success")

    def test(self):
        frames = self.driver.find_elements(By.TAG_NAME, "iframe")
        print(len(frames))

        self.driver.switch_to.frame(0)
        self.driver.switch_to.default_content()



    def validateTitle(self, expectedTitle):
        actualTitle = self.driver.title
        if (expectedTitle == actualTitle):
            self.reportSuccess("Title validation success...")
        else:
            self.reportFailure("Title validation not success..")

    def getRowNumberByName(self, locatorKey, userName):
        obj = self.prop[locatorKey]

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
                    return index + 1
            return -1

    def clickElementByRowNum(self, rowNum, locatorKey1, locatorKey2):
        obj1 = self.prop[locatorKey1]
        obj2 = self.prop[locatorKey2]

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
        obj = self.prop[locatorKey]

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
        obj = self.prop[locatorKey]

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

        obj = self.prop[locatorKey]
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