#import webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#driver = webdriver.Chrome("F:\chromedriver_win32\chromedriver.exe") # using absolute path
#service_obj = Service("./../driver/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome(service=Service("./../driver/chromedriver.exe"))

