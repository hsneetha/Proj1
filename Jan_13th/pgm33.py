import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL & wait till the page is loaded
driver.get("https://demo.actitime.com/login.do")
time.sleep(1)
#using selenium we cant take screenshot of desktop and by default it is the webpage(so no address age is seen)
driver.get_screenshot_as_file("loginpage.png")