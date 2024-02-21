# "conftest.py" file    --> generalize the fixture for global scope
# the fixture defined in this file will be available to all the test files under the same package/folder

import pytest


@pytest.fixture()           # fixture  --> it acts like the pre-requisite; set-up & tear-down method
def setup():                            # this method will run before the test that it attached to
    print("I will be executed first")   # --> set-up step
    yield                               # any code after "yield" will be executed after the test execution is completed
    print("I will be executed last")    # --> tear-down step


@pytest.fixture(scope="class")          # this fixture scope is in class level
def setup1():
    print("I will be executed first")   # --> only run once before the class is initialized
    yield
    print("I will be executed last")    # --> only run once after all test cases in the class being executed


###
# data-driven   --> can be done with return statement in tuple format
@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Ryan", "Gosling", "google.com"]        # pass the data from here to the test; returning a list (try tuple?)


###
# parameterization  --> can be done with return statement in tuple format
# pass the multiple datasets ino a fixture,
# so it will know to run the test case in multiple times, and every time have to pick one dataset
@pytest.fixture(params=[("Chrome", "hi", "bye"), ("Firefox", "cheers"), ("Edge")])   # fixture is parameterized
# first time, fixture would pick "("Chrome", "hi", "bye")" in first run, and give it to the test case
# second time, this fixture would invoke the test case again by passing "("Firefox", "cheers")" as an input
# third time, the fixture would take "("Edge", "huh")" as input
# --> run test with multiple dataset to achieve parameterization
def crossBrowser(request):          # send the picked data to this parameter "request" instance in each time
    return request.param            # send the data
