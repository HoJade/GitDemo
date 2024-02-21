import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup") # need not to explicitly define this fixture as the BaseClass has knowledge about it
class TestOne(BaseClass):           # inheriting the parent class "BaseClass" properties into the child class "TestOne"

    def test_e2e(self):

        log = self.getLogger()              # call the logging feature method from the parent class "BaseClass"

        homePage = HomePage(self.driver)                            # send "driver" as an argument to the constructor

        checkoutPage = homePage.shopItems()  # this method would return the object for next page; class = "CheckOutPage"
        # when clicked on "shopItems()", the web would land on "checkOutPage"
        # so, the very next item after clicking on "shopItem()" is to create "checkOutPage" object for its class
        # then, can use the object for that specific page
        # so, the "shopItems()" button is a transition point of two different pages
        # hence, the very next step is not required as it is handled in "shopItems()" method
        # checkOutPage = CheckOutPage(self.driver)

        log.info("Getting the product name")

        # track down the targeted item through a list scanning
        products = checkoutPage.getProductTitles()                  # return list of web elements
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text       # reach down the block, then grab text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()            # click to select if matches
                log.info(productName)

        checkoutPage.proceedCheckOut().click()

        confirmPage = checkoutPage.checkOutItems()          # transition point; from CheckOutPage to ConfirmPage

        log.info("Entering the country name as rus")
        # confirmPage = ConfirmPage(self.driver)            # integrated into the "checkOutItems()" method
        confirmPage.enterDeliveryLocation().send_keys("rus")

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Russia")))
        self.verifyLinkPresence("Russia")
        confirmPage.selectDeliveryLocation().click()

        confirmPage.checkCheckbox().click()
        confirmPage.clickPurchaseButton().click()

        successText = confirmPage.verifySuccessMessage().text
        log.info("Text received from application is " + successText)
        assert "Success! Thank you!" in successText

        '''
        to validate the element in console

        $x("//button[@class='btn btn-success']")        # XPATH
        $("//button[@class='btn btn-success']")         # CSS_SELECTOR
        
        ---
        to select web browser to run the test case during runtime in terminal
        
        py.test --browser_name chrome
        '''