import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


# can use this BaseClass to define all the custom utilities, which can be re-used across multiple test cases
@pytest.mark.usefixtures("setup")
class BaseClass:

    # explicit wait
    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))   # "Russia"

    def selectOptionByText(self, locator, text):
        # when see <select> tag for dropdown, then that's a static dropdown
        # if see <select> tag,then use the "Select" class to handle the options in that dropdown
        dropdown = Select(locator)                      # locator --> "homePage.expandStaticDropDown()"
        dropdown.select_by_visible_text(text)           # "Female"
        # dropdown.select_by_index(0)                 # select the 1st index
        # dropdown.select_by_value()                  # <option value="xxx">

###
    # logging feature function
    def getLogger(self):
        loggerName = inspect.stack()[1][3]          # capture the method name into "loggerName" of the method being call
        logger = logging.getLogger(loggerName)      # the log message will capture the test case name in the log file
        fileHandler = logging.FileHandler("logfile.log")    # fileHandler object  --> tell the log file name
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")     # log message format
        fileHandler.setFormatter(formatter)         # pass/connect the formatter object into the "fileHandler" object

        # how the file is presented; where to print & what is the format
        logger.addHandler(fileHandler)  # fileHandler object

        # set the log message level
        logger.setLevel(logging.DEBUG)

        return logger
