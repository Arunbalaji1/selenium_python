from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Ensure the path to your ChromeDriver executable is correct
chrome_driver_path = r'D:\ARUN\Selenium_learning\selenium_python\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)

# Initialize the WebDriver with the service
driver = webdriver.Chrome(service=service)
# Open the working website
driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)

#opening the dropdown
element = driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[11]/a")
element.click()
time.sleep(2)
#finding dropdown and selecting option1 
dropdown = Select(driver.find_element(By.ID,"dropdown"))
time.sleep(2)
dropdown.select_by_visible_text("Option 1")
#print result of the process
print("Selected Option 1")
time.sleep(2)
driver.quit()