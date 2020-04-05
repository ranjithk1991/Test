import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\Users\\Ranjit\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.expedia.co.in")
print("Launching.. ", driver.title)

driver.find_element_by_xpath("//*[@id='tab-hotel-tab-hp']/span[1]").click()

Going_to = driver.find_element_by_id('hotel-destination-hp-hotel')
Going_to.clear()
Going_to.send_keys("HK")

start_date = driver.find_element_by_name('startDate')
start_date.clear()
start_date.send_keys('11/04/2020')

end_date = driver.find_element_by_xpath("//*[@id='hotel-checkout-hp-hotel']")
end_date.send_keys('12/04/2020')

driver.find_element_by_xpath("//*[@id='gcw-hotel-form-hp-hotel']/div[11]/label/button").click()
wait = WebDriverWait(driver, 30)
prc_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='radio-sort-PRICE_LOW_TO_HIGH']")))
prc_btn.click()
time.sleep(3)
driver.quit()
