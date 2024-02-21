from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()     # create locator based upon the text

# collect all veggie names -> BrowserSorted_veggieList
BrowserSorted_veggieList = []
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")        # extracted the web element only
for ele in veggieWebElements:
    BrowserSorted_veggieList.append(ele.text)                           # get the "text" property from the element

originalBrowserSorted_veggieList = BrowserSorted_veggieList.copy()      # .copy() --> create a new copy of a list

# sort the BrowserSorted_veggieList -> newSortedList
# .sort()  --> the original list itself would be sorted, and would not generate a new list
BrowserSorted_veggieList.sort()                 # cannot assign a variable to collect the sorted list

# BrowserSorted_veggieList == newSortedList
assert originalBrowserSorted_veggieList == BrowserSorted_veggieList
