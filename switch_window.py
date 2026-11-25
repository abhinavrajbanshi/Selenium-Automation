#Script to switch windows or window handling

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
url="https://formy-project.herokuapp.com/switch-window"
driver.get(url)
time.sleep(2)

#Switch Window
switch_window=driver.find_element(By.ID, "new-tab-button")
switch_window.click()
time.sleep(2)

#Window Handling
window=driver.window_handles
print(window)
print("This is the current window", driver.current_window_handle)

#Switching Window
driver.switch_to.window(window[1])
print("The driver has switched to this window", driver.current_window_handle)
driver.find_element(By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Autocomplete']").click()
time.sleep(2)

driver.quit()