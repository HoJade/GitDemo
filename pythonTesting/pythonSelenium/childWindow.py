# open new tab = open new window

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Firefox(service=service_obj)

driver.implicitly_wait(2)


# explicitly wait for the webpage
wait = WebDriverWait(driver, 5)
driver.get("https://the-internet.herokuapp.com/windows")
wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))            # tag_name <h3>
print(driver.find_element(By.TAG_NAME, "h3").text)

driver.find_element(By.LINK_TEXT, "Click Here").click()         # <a> tag = anchor; indicate the "link text"


# get all the window names which are opened, and put it into a list
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])           # switch to another window (child window); argument --> window name
print(driver.find_element(By.TAG_NAME, "h3").text)              # tag_name <h3>
driver.close()                                      # close the child window, not the parent window

driver.switch_to.window(windowsOpened[0])           # switch back to the parent window
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
