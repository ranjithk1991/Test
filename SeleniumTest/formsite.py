import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Ranjit\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
print(driver.title)

text_boxes = driver.find_elements(By.CLASS_NAME, "text_field")
print(len(text_boxes))

drop = Select(driver.find_element_by_id("RESULT_RadioButton-9"))
print(drop.options)

for op in drop.options:
    print(op.text)

#drop.select_by_value('Radio-2')
drop.select_by_visible_text("Morning")

links = driver.find_elements(By.TAG_NAME, 'a')

for link in links:
    print(link.text)

Register = driver.find_element(By.LINK_TEXT, "Register").click()

time.sleep(5)
driver.quit()

