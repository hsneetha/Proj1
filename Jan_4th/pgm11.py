import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/selenium_pgms_BhanuSir/Demo1.html")
time.sleep(5)

#element=driver.find_element(By.TAG_NAME,"a")
#element.click()

driver.find_element(By.TAG_NAME,"a").click()
time.sleep(5)
driver.back()
time.sleep(2)

driver.find_element(By.ID,"a1").click()
time.sleep(5)
driver.back()
time.sleep(2)

driver.find_element(By.NAME,"n1").click()
time.sleep(5)
driver.back()
time.sleep(2)
#driver.find_element(By.ID,"a1").click()

#driver.find_element(By.NAME,"n1")

#driver.find_element(By.LINK_TEXT,"aksharatraining").click()


time.sleep(5)