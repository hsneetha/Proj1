import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
time.sleep(2)
driver.get("http://www.google.com")
time.sleep(2)
driver.switch_to_window("tab")
time.sleep(2)
driver.get("http://www.fb.com")
time.sleep(2)
driver.quit()
time.sleep(10)
