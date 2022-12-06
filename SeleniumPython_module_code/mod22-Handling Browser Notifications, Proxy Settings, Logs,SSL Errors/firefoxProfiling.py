from selenium import webdriver
#desired capabilities
#pageLoadStrategy
from selenium.webdriver import DesiredCapabilities

caps = DesiredCapabilities().FIREFOX
caps['pageLoadStrategy']=None

driver = webdriver.Firefox(desired_capabilities=caps)

fp = webdriver.FirefoxProfile("C:\\Users\\Abhishek\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dslne5iu.Jaspreet")
fp.set_preference("dom.webnotification.enabled",False)
fp.accept_untrusted_certs = True

driver = webdriver.Firefox(fp)
driver.get("https://web-push-book.gauntface.com/demos/notification-examples/")
