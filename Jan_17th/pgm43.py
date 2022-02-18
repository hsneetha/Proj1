import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.color import Color
#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL & wait till the page is loaded
driver.get("file:///F:/selenium_pgms_BhanuSir//Demo1_Jan17th.html")
time.sleep(2)
driver.execute_script("document.getElementById('un').value='Ravi';")

time.sleep(3)