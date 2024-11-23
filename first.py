from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Ensure the path to your ChromeDriver executable is correct
chrome_driver_path = r'D:\ARUN\Selenium_learning\selenium_python\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)

# Initialize the WebDriver with the service
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Print the title of the page

print(driver.title)
wait = WebDriverWait(driver, timeout=2)
wait.until(False)
driver.refresh()

""" driver.back()
driver.forward() """



