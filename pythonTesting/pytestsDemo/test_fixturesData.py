# fixture in "conftest.py" file
import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self, dataLoad):       # have to add the fixture parameter when returning the data to test
        print(dataLoad)
        print(dataLoad[0])


###
def test_crossBrowser(crossBrowser):            # this test will run multiple (three) times, because it is parameterized
    print(crossBrowser)
    print(crossBrowser[1])
