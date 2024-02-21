import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

# singular  --> default select the 1st element
driver.find_element(By.ID, "autosuggest").send_keys("ho")

time.sleep(2)       # wait 2 sec

# plural    --> identify all the elements, and return as a list
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

print(len(countries))         # count the number of items present in the list

# Dynamic Dropdown
for country in countries:
    if country.text == "Hong Kong":         # .text  --> extract the text present on that element
        country.click()
        break           # when the condition is met, then no need to keep iterating the loop

# print(driver.find_element(By.ID, "autosuggest").text)       # cannot extract the dynamically script-input text

# listen actively to the dynamically script-inserted value
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Hong Kong"
