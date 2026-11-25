#Script to screenshot mechanism

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

#Screenshot
login_button.screenshot("Login_button.png")
login_button.click()
time.sleep(1)
driver.save_screenshot("SwagLab_login.png")

driver.quit()