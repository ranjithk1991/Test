from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Ranjit\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://accessibility.umn.edu/web-designers/tables-web-pages/")
print(driver.title)

rows = len(driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div[3]/div/div/div/div[2]/section[1]/div/div/div/div[2]/div/div/div/table[2]/tbody/tr"))
print(rows)

cols = len(driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div[3]/div/div/div/div[2]/section[1]/div/div/div/div[2]/div/div/div/table[2]/tbody/tr[1]/td"))
print(cols)

for row in range(1, rows+1):
    for col in range(1, cols+1):
        table = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div[3]/div/div/div/div[2]/section[1]/div/div/div/div[2]/div/div/div/table[2]/tbody/tr["+str(row)+"]/td["+str(col)+"]").text
        print(table, end='   ')
    print()

driver.quit()