from pages.base import BasePage
from pages.loginPage import login


class landingPage(BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def landingpage(self):
        url = self.prop['URL']
        expectedTitle = self.prop['expectedTitle']
        self.navigate(url)
        self.wait()
        self.validateTitle(expectedTitle)
        self.wait()
        return login(self.driver)