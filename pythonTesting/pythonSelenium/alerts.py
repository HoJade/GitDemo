from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "Yannie"

service_obj = Service()
driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

# --> to handle browser(-based) alert / java alert / javascript alert, which prevent access of the web browser
# switch from browser mode to alert mode
alert = driver.switch_to.alert              # only focus on the alert but not on the browser level
alertText = alert.text                      # grab the text which is present on the alert
print(alertText)
assert name in alertText

alert.accept()                              # a method to click on [OK]; means Positive
# alert.dismiss()                             # a method to click on [Cancel]; means Negative
