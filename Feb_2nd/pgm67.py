import time
from selenium import webdriver


where_to_run="https://oauth-hsneetha-771ca:e8318446-469f-4ae2-9b56-84576317c4c1@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
which_browser_to_open=webdriver.ChromeOptions()

driver=webdriver.Remote(command_executor=where_to_run,options=which_browser_to_open)
driver.get("http://www.google.com")
print(driver.title)
time.sleep(2)
driver.close()

#https://oauth-hsneetha-771ca:e8318446-469f-4ae2-9b56-84576317c4c1@ondemand.eu-central-1.saucelabs.com:443/wd/hub