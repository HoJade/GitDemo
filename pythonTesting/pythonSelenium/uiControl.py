from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

# Checkbox
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":    # .get_attribute  --> get the "value" attribute, check its value
        checkbox.click()
        assert checkbox.is_selected()          # assertion to check is selected or not; it returns boolean
        break

# Radio button
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[1].click()
assert radiobuttons[1].is_selected()

# Display
# .is_displayed  --> check is displayed or not; returns boolean
assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
