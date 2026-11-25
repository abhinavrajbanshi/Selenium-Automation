#Script to Scroll Mechanism

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
url="https://formy-project.herokuapp.com/scroll"
driver.get(url)
time.sleep(2)

#Scroll
driver.execute_script("window.scrollBy(0,700);")
time.sleep(2)
driver.find_element(By.ID, "name").send_keys("Abhinav Rabanshi")
driver.find_element(By.ID, "date").send_keys("10/12/2005")
time.sleep(2)
driver.execute_script("window.scrollTo(0,0);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

driver.quit()