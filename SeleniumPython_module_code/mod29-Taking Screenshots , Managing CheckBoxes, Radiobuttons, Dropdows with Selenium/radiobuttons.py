import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/jobs-in-sydney-ns?trk=homepage-basic_intent-module-jobs&position=1&pageNum=0")
driver.implicitly_wait(10)

radiobuttons = driver.find_elements_by_name("sortBy")
print("Total no. of radio buttons : "+str(len(radiobuttons)))

for i in range(0, len(radiobuttons)):
    check = radiobuttons[i].get_attribute("checked")
    print(check)

driver.save_screenshot("radiobuttons.png")


time.sleep(5)
driver.quit()