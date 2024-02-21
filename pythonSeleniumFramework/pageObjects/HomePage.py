from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    # create a local constructor for this particular class
    # a constructor which accepts "driver" as an argument
    # so, whenever create an object for this class, have to pass "driver" as an argument
    # the "driver" from the test case will be assigned to this local class "driver"
    def __init__(self, driver):
        self.driver = driver

    # declared a page object
    shop = (By.CSS_SELECTOR, "a[href*='shop']")          # argument -->  (type of locator, actual locator)
    # Regular Expression -- "*=" --> target the partial value

    ###
    # test_HomePage.py
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    submitButton = (By.XPATH, "//input[@type='submit']")
    twoWayDataBindingExample = (By.XPATH, "(//input[@type='text'])[3]")
    name = (By.CSS_SELECTOR, "input[name='name']")
    radioButton = (By.CSS_SELECTOR, "#inlineRadio1")
    staticDropDown = (By.ID, "exampleFormControlSelect1")
    successMessage = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
    # after this method, the web would jump into next page
        # shop is a class variable  --> "HomePage.shop"
        # return --> send back to the call   self. --> access instance variable   *  --> de-serialize the tuple variable
        self.driver.find_element(*HomePage.shop).click()
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
        # driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()    # XPATH
        checkoutPage = CheckOutPage(self.driver)            # creating object for the next page; class = "CheckOutPage"
        return checkoutPage

    ###
    # test_HomePage.py
    def enterEmail(self):
        return self.driver.find_element(*HomePage.email)
        # driver.find_element(By.NAME, "email")

    def enterPassword(self):
        return self.driver.find_element(*HomePage.password)
        # driver.find_element(By.ID, "exampleInputPassword1")

    def clickCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)
        # driver.find_element(By.ID, "exampleCheck1")

    def clickSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)
        # driver.find_element(By.XPATH, "//input[@type='submit']")

    def enterTwoWayDataBindingText(self):
        return self.driver.find_element(*HomePage.twoWayDataBindingExample)
        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]")       # identify the 3rd element

    def enterName(self):
        return self.driver.find_element(*HomePage.name)
        # driver.find_element(By.CSS_SELECTOR, "input[name='name']")

    def clickRadioButton(self):
        return self.driver.find_element(*HomePage.radioButton)
        # driver.find_element(By.CSS_SELECTOR, "#inlineRadio1")

    def expandStaticDropDown(self):
        return self.driver.find_element(*HomePage.staticDropDown)
        # driver.find_element(By.ID, "exampleFormControlSelect1")

    def verifySuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)
        # driver.find_element(By.CLASS_NAME, "alert-success")
