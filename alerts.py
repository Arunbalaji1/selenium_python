from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
# the path of ChromeDriver t
chrome_driver_path = r'D:\ARUN\Selenium_learning\selenium_python\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)
# Initialize the WebDriver with the service
driver = webdriver.Chrome(service=service)
# Open the working website
driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)
element=driver.find_element(By.XPATH,"/html/body/div[2]/div/ul/li[29]/a")
element.click()
time.sleep(2)

#BUTTON1
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/ul/li[1]/button").click()
time.sleep(3)
alert = driver.switch_to.alert
print(alert.text)  # Print alert message
alert.accept()  # Accept the alert

#BUTTON2
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/ul/li[2]/button").click()
time.sleep(3)
alert = driver.switch_to.alert
print(alert.text)  # Print alert message
alert.accept()  # Accept the alert

#BUTTON 3
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/ul/li[3]/button").click()
time.sleep(3)
alert = driver.switch_to.alert
print(alert.text)  # Print alert message
alert.accept()  # Accept the alert
driver.quit()