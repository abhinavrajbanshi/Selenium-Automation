#Import Webdriver
from selenium import webdriver
import time

#Initialize chrome with webdriver
driver=webdriver.Chrome()
time.sleep(3)

#Maximize Window
driver.maximize_window()

#Navigate to URL
url="https://www.google.com/"
driver.get(url)
time.sleep(2)
print("The current url is ",driver.current_url)
print("The title name is ",driver.title)
driver.get("https://www.saucedemo.com/")
time.sleep(2)
print("The current url is ",driver.current_url)
print("The title name is ",driver.title)

#Refresh browser/window
driver.refresh()
time.sleep(1)

#Browser back/forward
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)

#Quit Driver
driver.quit()