from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    deliveryLocation = (By.ID, "country")
    locationOption = (By.LINK_TEXT, "Russia")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR, "[type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")

    def enterDeliveryLocation(self):
        return self.driver.find_element(*ConfirmPage.deliveryLocation)
        # self.driver.find_element(By.ID, "country")

    def selectDeliveryLocation(self):
        return self.driver.find_element(*ConfirmPage.locationOption)
        # self.driver.find_element(By.LINK_TEXT, "Russia")

    def checkCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def clickPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)
        # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")      # tag name is optional, if it's not shared
        # driver.find_element(By.XPATH, "//*[@type='submit']").click()            # XPATH

    def verifySuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)
        # self.driver.find_element(By.CLASS_NAME, "alert-success")
