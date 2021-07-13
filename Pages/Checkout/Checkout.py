from Base.BaseMetods import BaseMethodDrivers
from Pages.Confirm.Confirm import ConfirmPage
from Utilities import custon_logging as cl
import logging


class CheckoutPage(BaseMethodDrivers):
    log = cl.loggingtest(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    __selectedbrandname = "//h4[@class='media-heading']/a"
    __priceselected = "//table[contains(@class, 'table')]//td[3]/strong"
    __amountselected = "//table[contains(@class, 'table')]//td[4]/strong"
    __totalamount = "//h3/strong"
    __finalcheckout = "//button[contains(@class, 'btn-success')]"

    def validatebrand(self,brand):
        selbrandname=self.getText(self.__selectedbrandname, "xpath")
        if brand==selbrandname:
            return True
        else:
            return False

    def validateselectedamount(self):
        price = self.getText(self.__priceselected, "xpath")
        numprice = price[3:]
        amount = self.getText(self.__amountselected, "xpath")
        numamount = amount[3:]
        totalamount = self.getText(self.__totalamount, "xpath")
        numtotalamount = totalamount[3:]
        if 1*int(numprice)==int(numamount)==int(numtotalamount):
            return True
        else:
            return False

    def clickCheckoutagain(self):
        self.clickelement(self.__finalcheckout, "xpath")
        cn = ConfirmPage(self.driver)
        return cn
