# https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# set the behaviour and provide instructions on how the browser should be invoked
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")         # start the browser in maximized mode
chrome_option.add_argument("headless")                  # will not see the browser invocation in frontend
chrome_option.add_argument("--ignore-certificate-errors")   # ignore SSL certification error to access actual web-page


service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_option)    # give "options" to the browser invocation step

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
