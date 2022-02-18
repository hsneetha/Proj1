import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.relative_locator import locate_with
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/selenium_pgms_BhanuSir/Table2.html")

#get the subject above 'API'(above subject)
xp="//td[.='API']"
api_element=driver.find_element(By.XPATH,xp)


subject=driver.find_element(locate_with(By.TAG_NAME,"td").above(api_element)).text
print(subject)

time.sleep(3)
