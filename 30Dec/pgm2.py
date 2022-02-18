import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#code optimized to install chrome and launch the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#to enter URL
driver.get("http://www.google.com")
#fullscreen window()
size = driver.get_window_size() # to get the height and width of teh window
print(size)
time.sleep(5)
driver.set_window_size(300,500)

time.sleep(5)
position=driver.get_window_position() #get the current position (x,y) of the browser
print(position)

driver.set_window_position(350,450) # re-size the winodw position
time.sleep(5)
driver.close()