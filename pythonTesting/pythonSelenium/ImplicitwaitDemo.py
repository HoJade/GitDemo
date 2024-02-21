import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Firefox(service=service_obj)

# Implicit wait
# declare a global implicit wait time-out object, which would apply to each and every line in the code
driver.implicitly_wait(5)       # wait max. 5 sec for the element to show-up; if shown-up in 2 sec, saved 3 sec

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.find_element  --> search from the entire page
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)                   # always wait 2 sec

# .find_elements  --> would not get caught by the .implicitly.wait
# --> because if no element is found, it will return an empty list, which is still valid
# .implicitly_wait  --> won't check whether the list has item/element or not
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")       # find all the elements
count = len(products)
print(count)
assert count > 0

# for each item in the "products" list
for product in products:
    # chaining  --> find child element from the parent element
    # full path: //div[@class='products']/div/div/button
    product.find_element(By.XPATH, "div/button").click()       # searching down in each "product" element block

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
# create locator based upon the text on the element
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
assert driver.find_element(By.CLASS_NAME, "promoInfo").text == "Code applied ..!"
