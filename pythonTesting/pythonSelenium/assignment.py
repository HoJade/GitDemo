from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
# go to the child window
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

# parse the email from a sentence
message = driver.find_element(By.CSS_SELECTOR, ".red").text
chopMessage = message.split("at")
print(chopMessage)
email = chopMessage[1].strip().split(" ")[0]
print(email)

# paste the text to sign-in
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

# grab the error message
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[style='display: block;']")))
errorMessage = driver.find_element(By.CSS_SELECTOR, "div[style='display: block;']").text
print(errorMessage)