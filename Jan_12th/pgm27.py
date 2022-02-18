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
status=driver.find_element(By.ID, "input[id='A6']").click()
print(status)
time.sleep(3)
