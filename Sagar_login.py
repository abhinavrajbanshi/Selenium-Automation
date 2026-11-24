#Sagar Login page automation
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.maximize_window()
url="https://sagar-test-qa.vercel.app/"
driver.get(url)

#Explicity wait
wait=WebDriverWait(driver,10)

#Locators
username=driver.find_element(By.ID, "username")
#password=driver.find_element(By.ID, "password")
password=wait.until(EC.visibility_of_element_located((By.ID, "password")))
#login_button=driver.find_element(By.ID, "login-button")
login_button=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))


#Actions
username.send_keys("standard_user")
password.send_keys("secret_sauce")
time.sleep(1)
login_button.click()
time.sleep(2)

#Alert
alert=driver.switch_to.alert
alert.accept()
time.sleep(2)

driver.quit()