import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#de_path = ChromeDriverManager().install()
#driver = webdriver.Chrome(service=Service(de_path))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#open a url
driver.get("https://www.google.com/")
#get current title of the page
print(driver.title)
#get the current urlof the page
print(driver.current_url)
time.sleep(2)
#get the html code of the webpage
#print(driver.page_source)

