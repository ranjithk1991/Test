import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\Ranjit\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
print("Launching..", driver.title)
time.sleep(3)

username = driver.find_element_by_name("userName")
print("Username is available?", username.is_displayed())
username.send_keys("mercury")

pwd = driver.find_element_by_name("password")
print("Password field is enabled and displayed?", pwd.is_displayed())
pwd.send_keys("mercury")

login_btn = driver.find_element_by_name("login")
print("Login button visible?", login_btn.is_enabled())
login_btn.click()

if driver.title != "Welcome":
    print("Login Successful")
else:
    print("Login Failed")

roundtrip = driver.find_element_by_css_selector("Input[value=roundtrip]")
print("Roundtrip radio btn is selected?", roundtrip.is_selected())

oneway = driver.find_element_by_css_selector("Input[value=oneway]")
print("One Way radio btn is selected", oneway.is_selected())

time.sleep(6)
driver.close()
