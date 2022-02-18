import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#closes-closes current browser
#quit-closes all browser

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.naukri.com")
time.sleep(5)
driver.quit()
