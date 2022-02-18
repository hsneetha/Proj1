import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#open the browser; enter the URL
driver.get("file:///F:/selenium_pgms_BhanuSir//element.html")
time.sleep(1)
#find the element
time.sleep(1)
status=driver.find_element(By.ID,"A5").is_selected()
print(status) #True
status=driver.find_element(By.ID,"A6").is_selected()
print(status) #False
time.sleep(1)
status=driver.find_element(By.ID,"A1").is_enabled()
print(status)#True
status=driver.find_element(By.ID,"A4").is_enabled()
print(status) #False
time.sleep(1)
status=driver.find_element(By.ID,"A1").is_displayed()
print(status) #True
status=driver.find_element(By.ID,"A3").is_displayed()
print(status) #False
time.sleep(1)
