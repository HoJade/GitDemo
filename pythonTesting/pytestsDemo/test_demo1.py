# any pytest file should start with "test_" or end with "_test"
# pytest function/test method name should start with "test"
# code should be wrapped in method only
# every method is treated as one test case
# method name should make sense


'''
to run test in terminal

to run all the tests in the specific package
1. navigate and copy the package/folder path
2. in terminal, "cd" to that specific path
3. execute command "py.test" to run all the tests in that specific package/folder
    "py.test -v"        --> gives more information about the test case result execution in the log
    "py.test -v -s"     --> print the console.log in the output
    "py.test test_demo1.py"     --> only run the "test_demo1.py" file
    "py.test -k second -v -s"   --> gives the regular regression name to specifically run the test case with that name
    "py.test -m smoke -v -s"    --> run the marked (tagged) "@pytest.mark.smoke" test case
    "py.test --html=report.html -v -s"    --> generate an HTML report for the test with the file name "report.html"
'''
import pytest


@pytest.mark.smoke          # marked the concatenated test case as "smoke"
def test_firstProgram():
    print("Hello")


@pytest.mark.xfail          # this test case will still run, but would not see the pass/fail result in reporting output
def test_secondProgram():
    print("Good Morning")
