from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")

# Locator: ID, XPATH, CSS_SELECTOR, CLASS_NAME, NAME, LINK_TEXT
# use "LINK_TEXT" when the text is wrapped as a link and with anchor tag --> <a>
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "password")     # provide the partial text, it will identify the full link

# XPATH
# if there's NO attribute or NO attribute is unique, then can use parent-child tag travel to reach to the element
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")

# CSS_SELECTOR
# parent-child travel to reach to the desired element; travel via tag_name here
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")

driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# XPATH
# create locator based upon the text on the element
# driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
