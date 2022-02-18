import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.relative_locator import locate_with
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/selenium_pgms_BhanuSir/Table2.html")

#checkbox is in leftside using absolute locator
xp="//td[.='Java']/..//input"
driver.find_element(By.XPATH,xp).click()
time.sleep(2)

#checkbox is in rightside using absolute locator
driver.get("file:///F:/selenium_pgms_BhanuSir/Table3.html")
xp="//td[.='Java']/..//input"
driver.find_element(By.XPATH,xp).click()
time.sleep(2)

#checkbox is in leftside using relative locator
#select the 'java checkbox'
driver.get("file:///F:/selenium_pgms_BhanuSir/Table2.html")
xp="//td[.='Java']"
java_element=driver.find_element(By.XPATH,xp)
driver.find_element(locate_with(By.TAG_NAME,"input").near(java_element)).click()
time.sleep(2)

#checkbox is in rightside using relative locator
driver.get("file:///F:/selenium_pgms_BhanuSir//Table3.html")
xp="//td[.='Java']"
java_element=driver.find_element(By.XPATH,xp)
driver.find_element(locate_with(By.TAG_NAME,"input").near(java_element)).click()
time.sleep(2)
