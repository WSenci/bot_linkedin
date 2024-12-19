from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.linkedin.com")

print(driver.title)

driver.quit()
