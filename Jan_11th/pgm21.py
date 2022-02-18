import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/selenium_pgms_BhanuSir/Table2.html")
xp="//td[.='Java']"
java_element=driver.find_element(By.XPATH,xp)

#relative_locator=locate_with(By.TAG_NAME, "input").to_left_of(java_element)
#driver.find_element(relative_locator).click()

driver.find_element(locate_with(By.TAG_NAME, "input").to_left_of(java_element)).click()
time.sleep(3)


