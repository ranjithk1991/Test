import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\Ranjit\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.expedia.co.in/")

flight_tab = driver.find_element_by_id("tab-flight-tab-hp")
flight_tab.click()

src = driver.find_element_by_id('flight-origin-hp-flight')
src.clear()
src.send_keys("SFO")

dest = driver.find_element_by_id('flight-destination-hp-flight')
dest.clear()
dest.send_keys("NYC")

startdate = driver.find_element_by_xpath("//*[@id='flight-departing-hp-flight']")
startdate.clear()
startdate.send_keys("11/04/2020")

enddate = driver.find_element_by_xpath("//*[@id='flight-returning-hp-flight']")
enddate.clear()
enddate.send_keys("12/04/2020")

driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[9]/label/button").click()

wait = WebDriverWait(driver, 10)
ele = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
ele.click()

time.sleep(10)

driver.quit()
