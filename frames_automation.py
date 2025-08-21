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
driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)
#opening the frames
element = driver.find_element(By.LINK_TEXT, "Frames")
element.click()
time.sleep(2)
#opening the nested frames
element = driver.find_element(By.LINK_TEXT, "Nested Frames")
element.click()
time.sleep(2)


# Switch to framecle
driver.switch_to.frame("frame-bottom")
name= driver.find_element(By.XPATH, "/html/body")
print(name.text)
driver.switch_to.default_content()
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-right")
name= driver.find_element(By.XPATH, "/html/body")
print(name.text)
driver.switch_to.default_content()
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-middle")
name= driver.find_element(By.XPATH, "/html/body")
print(name.text)
driver.switch_to.default_content()  # Switch back to main content

driver.quit()