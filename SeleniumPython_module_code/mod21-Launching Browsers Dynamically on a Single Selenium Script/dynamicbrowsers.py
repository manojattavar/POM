from selenium import webdriver

browsername = ""
webdriver.driver = None

if browsername == 'Chrome':
    driver = webdriver.Chrome()
elif browsername == 'Firefox':
    driver = webdriver.Firefox()
elif browsername == 'Edge':
    driver = webdriver.Edge()
elif browsername == 'IE':
    driver = webdriver.ie()
else:
    print("No browser specified.....")

try:
    if driver != None:
        driver.get("https://flipkart.com")
        driver.quit()
except NameError as n:
    print(n)