import logging
import time

from Base.BaseMetods import BaseMethodDrivers
from Utilities import custon_logging as cl


class ConfirmPage(BaseMethodDrivers):
    log = cl.loggingtest(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)

    __country= "country"
    __countrylist= "//div[@class='suggestions']//a"
    __submit = "//input[contains(@class, 'btn') and (@type='submit')]"
    __successmessage = "//div[contains(@class,'alert')]//strong"

    def updatecountry(self, country):
        self.senddata(country, self.__country, "id")

    def waitforcountry(self):
        self.waitforpresence(15, self.__countrylist, "xpath")

    def selectcountry(self, countryname):
        countries = self.getelementlist(self.__countrylist, "xpath")
        for count in countries:
            if count.text == countryname:
                count.click()
                break

    def clicksubmit(self):
        self.clickelement(self.__submit, "xpath")

    def validateordersuccess(self):
        message = self.getText(self.__successmessage, "xpath")
        if "Success" in message:
            return True
        else:
            return False

    def submitorder(self, country, countryname):
        self.updatecountry(country)
        self.waitforcountry()
        self.selectcountry(countryname)
        self.clicksubmit()
        time.sleep(4)