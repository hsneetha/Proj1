import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.google.com")

driver.switch_to.active_element.send_keys("python")

#element.send_keys("python")
time.sleep(15)

#cwdpt