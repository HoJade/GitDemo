import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):          # "BaseClass" will invoke the "setup" fixture in "conftest.py" file

    def test_formSubmission(self, getData):    # introduce the fixture as an argument, then it will load into the test

        # alternative, remove the URL from the "conftest.py" file, and load it inside the test
        # self.driver.get("https://rahulshettyacademy.com/angularpractice/")

        # the following codes have already been configured in the "conftest.py" file
        # service_obj = Service()
        # driver = webdriver.Chrome(service=service_obj)
        # driver.get("https://rahulshettyacademy.com/angularpractice/")

        log = self.getLogger()  # call the logging feature method from the parent class "BaseClass"

        homePage = HomePage(self.driver)
        log.info("email is " + getData["email"])
        homePage.enterEmail().send_keys(getData["email"])                 # "hello@gmail.com"
        homePage.enterPassword().send_keys(getData["password"])              # "123456"
        homePage.clickCheckbox().click()

        homePage.enterName().send_keys(getData["name"])                  # "hi"
        homePage.clickRadioButton().click()
        homePage.clickSubmitButton().click()

        homePage.enterTwoWayDataBindingText().send_keys(getData["2-way data binding text"])     # "bye"
        homePage.enterTwoWayDataBindingText().clear()           # clear the field

        # Static Dropdown
        # self.selectOptionByText(dropdown locator, option text "Female")
        self.selectOptionByText(homePage.expandStaticDropDown(), getData["gender"])

        message = homePage.verifySuccessMessage().text          # grab the text
        print(message)

        # assertion for validation
        assert "Success" in message

        # refresh the page
        self.driver.refresh()

###
# feed the data to only this test, so this specific fixture is not common to all test cases
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))     # call the static method from "HomePageData" class
    # (params=HomePageData.test_HomePage_Data) -->  call the variable "test_HomePage_Data" from the "HomePageData" class
    # inside the list, each tuple is treated as one test case
    # [("hello@gmail.com", "123456", "hi", "bye", "Female"), ("test@gmail.com", "223456", "hey", "bruh", "Male")]
    # tuple is used if want to pass value directly with index  --> getData[1] = "123456", ...
    def getData(self, request):         # to send the parameter back, "self" is required as it is inside a class
        return request.param
