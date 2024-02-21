from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Regular Expression -- "*=" --> target the partial value
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()         # CSS
# driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()    # XPATH


# track down the targeted item through a list scanning
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")     # return list of web elements
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text       # reach down the block, then grab text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()            # click to select if matches

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
# Regular Expression
# driver.find_element(By.XPATH, "//button[contains(@class,'btn-success')]").click()

driver.find_element(By.ID, "country").send_keys("rus")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Russia")))
driver.find_element(By.LINK_TEXT, "Russia").click()

driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()         # tag name is optional, if it's not shared
# driver.find_element(By.XPATH, "//*[@type='submit']").click()            # XPATH

successText = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in successText


'''
to validate the element in console

$x("//button[@class='btn btn-success']")        # XPATH
$("//button[@class='btn btn-success']")         # CSS_SELECTOR
'''