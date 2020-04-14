from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Ranjit\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.expedia.co.in/")
print(driver.title)

driver.find_element_by_id("travel-advisory-message-link").click()

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    print(driver.title)
