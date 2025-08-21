from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Ensure the path to your ChromeDriver executable is correct
chrome_driver_path = r'D:\ARUN\Selenium_learning\selenium_python\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)

# Initialize the WebDriver with the service
driver = webdriver.Chrome(service=service)
# Open the working website
a = "admin"
# appending username, password with URL
s = "https://" + a + ":" + a + "@" + "the-internet.herokuapp.com/basic_auth"
driver.get(s)
# identify text
m = driver.findElement(By.cssSelector("p")).getText()
print("Text is: " + m)
driver.close()