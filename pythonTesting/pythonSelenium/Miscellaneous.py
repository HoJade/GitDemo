from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# run in headless mode  --> no browser invocation; will not be able to see how the execution is running
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")

chrome_option.add_argument("--ignore-certificate-errors")       # auto-proceed the "Your connection is not private" page

service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_option)       # add one more argument "options"

driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# .execute_script()  --> execute JavaScript
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")      # scroll to the bottom

# take a screenshot to capture the current browser state and save the file in the folder
driver.get_screenshot_as_file("screenshot.png")
