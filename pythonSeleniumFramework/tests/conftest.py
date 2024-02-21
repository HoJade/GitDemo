# "conftest.py" file    --> generalize the fixture for global scope
# the fixture defined in this file will be available to all the test files under the same package/folder

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None           # declare a global "driver" object

# command line options:   https://docs.pytest.org/en/latest/example/simple.html
# --> declare and initialize the runtime variable
# this is a hook for adding the command line options
# key:  "--key"    value:  action="value"
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="option: chrome (default) / firefox / edge"
    )


@pytest.fixture(scope="class")          # scope = "class"; it will be called once before the class start executing
def setup(request):                     # "request" is the instance for this declared fixture

    global driver           # use the global "driver" object, which is defined at the top

    service_obj = Service()

    browser_name = request.config.getoption("browser_name")         # retrieve the value of option key in command line
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "firefox":                         # "elif" --> else if
        driver = webdriver.Firefox(service=service_obj)

    elif browser_name == "edge":
        driver = webdriver.Edge(service=service_obj)

    driver.implicitly_wait(2)
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    # tie up the "request" instance to the class instance (cls), because we used that fixture in class level
    request.cls.driver = driver         # assigning the local "driver" object to the class (cls) driver variable
    yield
    driver.close()


###
# have a screenshot beside the test failure in the report whenever the test fail
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
