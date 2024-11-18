from selenium import webdriver
url="https://www.google.com"

driver = webdriver.Chrome()
driver.get(url)   
print("page Title is:",driver.title)