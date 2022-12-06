import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://seleniumtraining.com")
driver.implicitly_wait(10)
dropdown = driver.find_element_by_id("userCountry")

select = Select(dropdown)
#check the default/all selected option
#all options available
#select/deselect - visible text, value, index
defaultselectedoption = select.first_selected_option
print(defaultselectedoption.text)

options = select.options
for i in range(0,len(options)):
    text = options[i].text
    print(text)

select.select_by_visible_text("Indonesia")
time.sleep(2)
select.select_by_value("2")
time.sleep(2)
select.select_by_index("10")
time.sleep(5)
driver.quit()