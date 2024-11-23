from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys 
import logging
import time
logging.basicConfig(filename="error_log.txt",level=logging.ERROR)
url="http://127.0.0.1:5500/main.html"
# Ensure the path to your ChromeDriver executable is correct
chrome_driver_path = r'D:\ARUN\Selenium_learning\selenium_python\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)

# Initialize the WebDriver with the service
driver = webdriver.Chrome(service=service)
driver.get(url)

try:
    driver.find_elemeeent(By.ID,"username")
except Exception as e:
    logging.error(f"NoSuchElementException: {e}")

username=driver.find_element(By.ID,"username")
password=driver.find_element(By.ID,"password")
username.send_keys("Arunbalaji")
password.send_keys("random79")
login_btn=driver.find_element(By.ID,"loginBtn")
login_btn.send_keys(Keys.RETURN)
""" cancel_btn=driver.find_element(By.NAME,"cancelBtn")
cancel_btn.send_keys(Keys.RETURN) """
time.sleep(1000)