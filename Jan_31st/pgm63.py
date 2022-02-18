import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# #enter the URL
driver.get("https://www.fb.com")

#open new window and goto google.com
driver.switch_to.new_window("tab")
driver.get("https://www.google.com")

#open new window and goto google.com
driver.close()
time.sleep(2)

