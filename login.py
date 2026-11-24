#Saucedemo Login page automation

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
url="https://www.saucedemo.com/"
driver.get(url)
time.sleep(2)
'''
ID Locators:
username= user-name
password= password
login button= login-button

X-path Locators:
uername=

Relative X-Path 
//*[@id="user-name"]
Absolute X-Path
/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input

password=

Relative X-Path
//*[@id="password"]
Absolute X-Path
/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[2]/input

login_button=

Relative X-path
//*[@id="login-button"]

'''
#Locators
username=driver.find_element(By.XPATH, "//*[@id='user-name']")
password=driver.find_element(By.XPATH, "//*[@id='password']")
login_button=driver.find_element(By.ID, "login-button")

#Actions
username.send_keys("standard_user")
password.send_keys("secret_sauce")
time.sleep(1)
login_button.click()
time.sleep(1)

if driver.current_url=="https://www.saucedemo.com/inventory.html":
    print("Login successful")
else:
    print("Login Failed")

#assert "inventory" in driver.current_url, "Login Failed!"

#DropDown
from selenium.webdriver.support.ui import Select
dropdown_menu=driver.find_element(By.XPATH, "//select[@aria-label='Sort products']")
select=Select(dropdown_menu)
select.select_by_value("lohi")
time.sleep(2)

driver.quit()
