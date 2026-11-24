#Saucedemo Login page automation
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
url="https://www.saucedemo.com/"
driver.get(url)
time.sleep(2)

#Explicity wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait=WebDriverWait(driver,10)

#Locators
username=driver.find_element(By.XPATH, "//*[@id='user-name']")
#password=driver.find_element(By.ID, "//*[@id='password']")
password=wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='password']")))
#login_button=driver.find_element(By.ID, "login-button")
login_button=wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

#Actions
username.send_keys("standard_user")
password.send_keys("secret_sauce")
time.sleep(2)
login_button.click()
time.sleep(2)

if driver.current_url=="https://www.saucedemo.com/inventory.html":
    print("Login successful")
else:
    print("Login Failed")
driver.quit()