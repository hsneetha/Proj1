import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#code optimized to install chrome and launch the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#to enter URL
driver.get("http://www.google.com")
#minimze window
driver.minimize_window()
time.sleep(5)
#maximize windw
driver.maximize_window()
time.sleep(5)
#clsoe the browser
driver.close()