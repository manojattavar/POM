import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.execute_script("window.location='https://edition.cnn.com/'")

# load_status=driver.execute_script("return document.readyState")
# print(load_status)

i=1
while(i!=10):
    load_status = driver.execute_script("return document.readyState")
    print(load_status)
    if(load_status=='complete'):
        break
    else:
        time.sleep(2)

i=1
while(i!=10):
    load_status = driver.execute_script("return jQuery.active")
    print(load_status)
    if(load_status==0):
        break
    else:
        time.sleep(2)

# el = driver.find_element_by_xpath("//*[@id='intl_homepage1-zone-4']/div[4]/div[1]/h2")
# print(el.location['x'])
# print(el.location['y'])
#
# driver.execute_script("window.scrollTo(0,2000)")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(5)
driver.quit()