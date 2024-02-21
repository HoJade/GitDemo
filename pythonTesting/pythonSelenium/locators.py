from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Locator: ID, NAME, CLASS_NAME, LINK_TEXT, TAG_NAME, XPATH, CSS_SELECTOR
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()


# XPATH
# //tagname[@attribute='value']  --> //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("bye")        # identify the 3rd element
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()                 # clear the field


# CSS_SELECTOR
# tagname[attribute='value']  --> input[type='submit'], #id, .class_name
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("hi")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()


# Static Dropdown
# when see <select> tag for dropdown, then that's a static dropdown
# if see <select> tag,then use the "Select" class to handle the options in that dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)                 # select the 1st index
# dropdown.select_by_value()                  # <option value="xxx">


message = driver.find_element(By.CLASS_NAME, "alert-success").text    # grab the text
print(message)

# assertion for validation
assert "Success" in message
