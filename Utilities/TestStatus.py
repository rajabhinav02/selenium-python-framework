import logging

from Base.BaseMetods import BaseMethodDrivers
from Utilities import custon_logging as cl


class testStatus(BaseMethodDrivers):
    log= cl.loggingtest(logging.DEBUG)

    def __init__(self, driver):
        super(testStatus,self).__init__(driver)
        self.driver = driver
        self.resultlist = []

    def testresult(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("Pass")
                    self.log.info("######### "+resultmessage + " is Pass")
                else:
                    self.resultlist.append("Fail")
                    self.log.error("######## "+resultmessage + " is FAIL")
                    self.getScreenshot(resultmessage)
            else:
                self.resultlist.append("Fail")
                self.getScreenshot(resultmessage)
                self.log.error("###### BLANK RESULT for "+resultmessage + " hence, FAIL")
                self.getScreenshot(resultmessage)
        except:
            self.resultlist.append("Fail")
            self.log.erroe("Issue with test result for "+resultmessage + " hence, FAIL")
            self.getScreenshot(resultmessage)

    def marktest(self, result, resultmessage):
        self.testresult(result, resultmessage)

    def marktestfinal(self, result, resultmessage, tcname):
        self.testresult(result, resultmessage)

        if "Fail" in self.resultlist:
            self.log.info("############## Test Case FAILED "+tcname)
            self.resultlist.clear()
            assert True==False
        else:
            self.log.info("############ Test Case PASSED "+tcname)
            self.resultlist.clear()
            assert True==True

