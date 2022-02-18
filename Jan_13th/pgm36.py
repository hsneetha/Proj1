import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL & wait till the page is loaded
driver.get("https://books-pwakit.appspot.com/")
time.sleep(2)
#find element present on the page which is inside the shadow_root section(under which shadow root starts)
main_element=driver.find_element(By.XPATH,"//book-app[@apptitle='BOOKS']")
#access the shadow root of the element
shadow_root=main_element.shadow_root
#find the element present inside the shadow root
shadow_root.find_element(By.CSS_SELECTOR,"#input").send_keys("bhanu")
time.sleep(4)
