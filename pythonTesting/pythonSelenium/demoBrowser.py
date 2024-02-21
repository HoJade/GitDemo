from selenium import webdriver                      # from a pacakge import a class
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.edge.service import Service

# script --> driver (proxy driver) --> browser

# --> Chrome
service_obj = Service()                             # start the driver service
driver = webdriver.Chrome(service=service_obj)      # start the browser

# --> Firefox
# service_obj = Service()
# driver = webdriver.Firefox(service=service_obj)

# --> Edge
# service_obj = Service()
# driver = webdriver.Edge(service=service_obj)

driver.maximize_window()                            # maximize the browser window
driver.get("https://google.com")                    # go to the website

print(driver.title)                                 # get the title of the window tab
print(driver.current_url)                           # get the current URL

driver.get("https://www.selenium.dev/")
driver.back()                                       # go back to the previous URL
driver.refresh()                                    # refresh the current page
driver.forward()                                    # go to the next browser page
driver.minimize_window()                            # minimize the browser window
driver.close()                                      # close the browser


# service_obj = Service()                           # Service("{{paste the file path of the downloaded driver}}")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://google.com")
