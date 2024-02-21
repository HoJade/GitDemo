# frame  --> another page / HTML component that embedded into the base/parent HTML

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Firefox(service=service_obj)

driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")                     # switch to frame; argument --> frame id/name
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")

# .default_content()  --> when driver is originally initiated
driver.switch_to.default_content()                      # switch back to default content; normal browser scope
print(driver.find_element(By.CSS_SELECTOR, "h3").text)      # enter the "tag name" directly for CSS_SELECTOR
