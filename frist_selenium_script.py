from selenium import webdriver
url="https://www.google.com/?authuser=2"

driver = webdriver.Chrome()
driver.get(url)   
print("page Title is:",driver.title)