import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
###important -HOME WORK

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#open the browser; enter the URL
driver.get("file:///F:/selenium_pgms_BhanuSir//element.html")
time.sleep(1)
#find the element
element1=driver.find_element(By.ID,'A1')
#clear the value
element1.clear()
time.sleep(1)
#enter the new value
element1.send_keys("akshara")
time.sleep(3)
