import pytest


# @pytest.fixture()           # fixture  --> it acts like the pre-requisite; set-up & tear-down method
# def setup():                            # this method will run before the test that it attached to
#     print("I will be executed first")   # --> set-up step
#     yield                               # any code after "yield" will be run after the test execution is completed
#     print("I will be executed last")    # --> tear-down step


def test_fixtureDemo(setup):            # this test will run the fixture as it has tied up in the argument
    print("I will execute steps in fixtureDemo method")


###
# declare the same fixture in the class level, so it will automatically apply to each and every method of that class
@pytest.mark.usefixtures("setup")       # fixture as argument; it will automatically apply to all methods in the class
class TestExample:                      # wrap the methods in class

    def test_fixtureDemo1(self):        # when declared method in class, "self" is a mandatory parameter
        print("I will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo2 method")


###
# run the fixture only once before the class, but not before each and every method/test case
@pytest.mark.usefixtures("setup1")
class TestExample1:

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo3 method")

    def test_fixtureDemo4(self):
        print("I will execute steps in fixtureDemo4 method")
