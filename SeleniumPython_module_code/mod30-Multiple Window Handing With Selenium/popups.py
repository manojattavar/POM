# s = {6,7,3,11,11,11,'Apple'}
# print(len(s))
# print(s)

# sets = iter(s)
# print(next(sets))
# print(next(sets))
# print(next(sets))
# print(next(sets))
# print(next(sets))
# print(next(sets))
# for i in range(0,len(s)):
#     print(next(sets))

# for i in sets:
#     print(i)

import time
from selenium import webdriver

driver = webdriver.Firefox()
windowid = driver.window_handles
print("")
driver.get("https://naukri.com/")
windowid = driver.window_handles

idSet = iter(windowid)
for i in windowid:
    print(i)
    driver.switch_to.window(i)
    driver.close()
    driver.switch_to.default_content()
    #close - window under focus
    #quit - all windows in session

time.sleep(5)
driver.quit()
