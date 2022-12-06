import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


def test_browser():
    chromeDriver = "C:\\Users\\029693744\\Desktop\\Selenium\\webdriver\\drivers\\chromedriver_win32\\chromedriver.exe"
    firefoxDriver = "C:\\Users\\029693744\\Desktop\\Selenium\\webdriver\\drivers\\geckodriver-v0.32.0-win32\\geckodriver.exe"

    # gridRun = "Y"
    browserName = 'Chrome'
    if (browserName == 'Chrome'):
        caps = DesiredCapabilities.CHROME.copy()
        caps['browserName'] = 'chrome'
        caps['javascriptEnabled'] = True
    elif (browserName == 'Firefox'):
        caps = DesiredCapabilities.FIREFOX.copy()
        caps['browserName'] = 'firefox'
        caps['javascriptEnabled'] = True

    driver = webdriver.Remote(desired_capabilities=caps, command_executor='')
    driver = webdriver.Chrome(executable_path=chromeDriver)
    driver.get("https://www.google.com")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()
