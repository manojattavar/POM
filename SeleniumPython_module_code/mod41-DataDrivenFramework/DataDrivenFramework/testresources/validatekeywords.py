'''
Created on 03-Jul-2020
@author: jaspreet
'''
import logging
from _datetime import datetime

from async_generator._tests import conftest


class validatekeywords():
    def __init__(self):
        self.prop = conftest.prop
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.ERROR)
        
    # def takeScreenshot(self):
    #     allure.attach(self.driver.get_screenshot_as_png(),"Screenshot at : "+str(datetime.now()),AttachmentType.PNG)
    
    def logging(self,message):
        self.logger.info(message)
    
    def reportFailure(self,message):
        self.takeScreenshot()
        assert False, message
    
    def reportSuccess(self,message):
        self.logging(message)
        assert True
        
    def ValidateTitle(self):
        with allure.step("Validating Page Title..."):
            expectedTitle = self.prop['expectedTitle']
            actualTitle = self.driver.title
            if(expectedTitle==actualTitle):
                self.reportSuccess("Title Matched... Page Title Validation Successful")
            else:
                self.reportFailure("Title Mismatch...Got title as "+actualTitle+ " instead of "+expectedTitle)
