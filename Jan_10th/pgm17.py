import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
###important -HOME WORK 

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#open the browser; enter the URL
driver.get("https://demo.actitime.com/login.do")
#enter the username
driver.find_element(By.ID, "username").send_keys("admin")
#enter the password
driver.find_element(By.NAME, "pwd").send_keys("manager")
#click on keepme loggedin checkbox
driver.find_element(By.ID, "keepLoggedInCheckBox").click()
#click on login button
driver.find_element(By.XPATH, "//div[.='Login ']").click()
time.sleep(5)
