import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Ranjit\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
print(driver.title)

links = driver.find_elements(By.TAG_NAME, 'a')

for link in links:
    print(link.text)

Register = driver.find_element(By.LINK_TEXT, "REGISTER").click()

time.sleep(5)

driver.quit()