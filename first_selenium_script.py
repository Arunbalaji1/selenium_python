from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Ensure the path to your ChromeDriver executable is correct
chrome_driver_path = r'D:\ARUN\Selenium_learning\selenium_python\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)

# Initialize the WebDriver with the service
driver = webdriver.Chrome(service=service)
# Specify the path to the ChromeDriver
# If ChromeDriver is not in your system PATH, provide the exact path to the driver

url = "https://www.google.com"
url2= 'https://www.amazon.com'

# Open Google

driver.get(url)

# Print the title of the current webpage
print("Page Title is: ", driver.title)

# Close the browser

driver.get(url2)
print("the web site name :",driver.title)
