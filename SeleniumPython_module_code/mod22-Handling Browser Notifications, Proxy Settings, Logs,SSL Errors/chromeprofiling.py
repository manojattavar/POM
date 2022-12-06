from selenium import webdriver

op = webdriver.ChromeOptions()
op.add_argument("user-data-dir=C:\\Users\\Abhishek\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
op.add_argument("--disable-bookmarks")
op.add_argument("--disable-notifications")
op.add_argument("--start-maximized")
op.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(options=op)
driver.get("https://news18.com/")