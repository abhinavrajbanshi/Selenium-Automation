#Saucedemo Mouse Action

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
url="https://www.saucedemo.com/"
driver.get(url)
time.sleep(2)

#Locators
username=driver.find_element(By.XPATH, "//*[@id='user-name']")
password=driver.find_element(By.XPATH, "//*[@id='password']")
login_button=driver.find_element(By.ID, "login-button")

#Actions
username.send_keys("standard_user")
password.send_keys("secret_sauce")
time.sleep(1)

#Action chain or mouse actions
from selenium.webdriver.common.action_chains import ActionChains
action=ActionChains(driver)
action.context_click(login_button).perform()
time.sleep(1)

if driver.current_url=="https://www.saucedemo.com/inventory.html":
    print("Login successful")
else:
    print("Login Failed")

#assert "inventory" in driver.current_url, "Login Failed!"

driver.quit()