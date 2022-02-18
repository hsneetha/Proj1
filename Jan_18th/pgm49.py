import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/selenium_pgms_BhanuSir//Demo1_Jan18th.html")

#find all the input elements
all_textbox=driver.find_elements(By.TAG_NAME,"input")
#count the input element
count=len(all_textbox) #10
print(count)

#get the 1st input element
first_input=all_textbox[0]
htmlcode=first_input.get_property("outerHTML")
print(htmlcode)

#get all the input elements one by one
for i in range(count):
  input=all_textbox[i]
  input.send_keys("bhanu")

for i in range(0,count):
    input = all_textbox[i]
    input.clear()
#below is efficient way to write the program by directly providing the text value
for textbox in all_textbox:
    textbox.send_keys("bhanu")

# to clear the elements in reverse order...count-1(9), -1(to remove even teh first text value); if we give zero it clears till
#1 an doesnt clear 0th one...last -1 is for reverse order
for i in range(count-1,-1,-1):
    input = all_textbox[i]
    input.clear()

time.sleep(3)
