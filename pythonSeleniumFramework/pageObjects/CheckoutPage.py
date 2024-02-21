from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    productTitles = (By.XPATH, "//div[@class='card h-100']")
    proceedCheckOutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    clickCheckOutButton = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductTitles(self):
        return self.driver.find_elements(*CheckOutPage.productTitles)
        # driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    def proceedCheckOut(self):
        return self.driver.find_element(*CheckOutPage.proceedCheckOutButton)
        # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.clickCheckOutButton).click()
        # confirmPage = ConfirmPage(self.driver)
        # return confirmPage
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        # Regular Expression
        # driver.find_element(By.XPATH, "//button[contains(@class,'btn-success')]").click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
