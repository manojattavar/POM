# s={5,8,2,6,9,"set","lists","apple"}
# print(len(s))
# print(s)
#
# s.add(5)
# print(len(s))

# sets = iter(s)
# print(next(sets))
# print(next(sets))
# print(next(sets))
# print(next(sets))
# print(next(sets))
# print(next(sets))
# print(next(sets))
# print(next(sets))
# for set in sets:
#     print(set)
#
# for i in range(0,len(s)):
#     print(next(sets))

'''
Created on 01-May-2020
@author: jaspreet
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
handles = set(driver.window_handles)
print(len(handles))
driver.get("https://www.naukri.com/")
handles = set(driver.window_handles)
print(len(handles))
print(driver.current_window_handle)
print("-----")
sets = iter(handles)
for i in sets:
    print(i)
    try:
        driver.switch_to.window(i)
        driver.close()
    except Exception as e:
        print(e)
    # finally:
    #     driver.switch_to.default_content()

# #close - close the window under focus
# #quit - closes all the windows in current session
#
# driver.switch_to.window(secondPopUp)
# driver.close()
#
# driver.switch_to.window(mainwindow)
# time.sleep(5)
# driver.quit()


