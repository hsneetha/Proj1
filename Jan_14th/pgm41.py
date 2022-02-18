import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL & wait till the page is loaded
driver.get("https://www.actimind.com/")
driver.maximize_window()
time.sleep(1)
h=driver.find_element(By.XPATH,"/html/body/header").size['height']
y=driver.find_element(By.XPATH,"//a[contains(text(),'Learn')]").location['y']
y=y-h
js_code="window.scrollBy(0," + str(y)+")"
print(js_code)
driver.execute_script(js_code)
time.sleep(5)
