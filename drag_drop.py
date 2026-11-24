#Drag and Drop Automation
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
url="https://formy-project.herokuapp.com/dragdrop"
driver.get(url)
time.sleep(2)

#Drag and Drop
from selenium.webdriver.common.action_chains import ActionChains
source=driver.find_element(By.XPATH, "//div[@id='image']//img")
destination=driver.find_element(By.XPATH, "//div[@id='box']")
action=ActionChains(driver)
action.drag_and_drop(source, destination).perform()
time.sleep(3)

driver.quit()