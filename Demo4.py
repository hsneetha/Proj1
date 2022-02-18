from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.firefox(service=Service(GeckoDriverManager().install()))


