from pytestsDemo.BaseClass import BaseClass


class TestExample2(BaseClass):          # pass/inherit parent class into child class

    def test_editProfile(self, dataLoad):       # have to add the fixture parameter when returning the data to test
        log = self.getLogger()          # get/call the inherited "getLogger" method
        log.info(dataLoad)              # this will log/print in the HTML report output
        print(dataLoad)                 # this will not log/print in the HTML report output
        log.info(dataLoad[2])
        print(dataLoad[2])
