# Import Selenium WebDriver
from selenium import webdriver

# Specify the path to the ChromeDriver
# If ChromeDriver is not in your system PATH, provide the exact path to the driver

url = "https://www.google.com"
url2= 'https://www.amazon.com'

# Open Google
driver = webdriver.Chrome()
driver.get(url)

# Print the title of the current webpage
print("Page Title is: ", driver.title)

# Close the browser
driver2 = webdriver.Chrome()
driver2.get(url2)
print("the web site name :",driver2.title)
print("the name of the user is guru")