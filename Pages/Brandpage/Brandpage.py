import logging
import time

from Base.BaseMetods import BaseMethodDrivers
from Pages.Checkout.Checkout import CheckoutPage
from Utilities import custon_logging as cl


class BrandPage(BaseMethodDrivers):
    log=cl.loggingtest(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __addbutton = "//button[contains(@class, 'btn-info')]"
    #__brandname = "//h4[@class='card-title']"
    __brandname = "parent::div/parent::div//h4/a"
    __checkout = "//a[contains(@class,'btn-primary')]"

    def clickadd(self, brand):

        buttons= self.getelementlist(self.__addbutton, "xpath")

        for button in buttons:
            bran = self.getxpathfromchild(button,self.__brandname).text
            #bran = button.find_element_by_xpath(self.__brandname).text
            if bran == brand:
                button.click()




        """
        brandnames = self.getelementlist(self.__brandname, "xpath")

        for brandn in brandnames:
            if brandn.text == brand:
                for button in buttons:

                    button.click()
                    time.sleep(4)
        """


    def clickcheckout(self):
        self.clickelement(self.__checkout, "xpath")
        ck = CheckoutPage(self.driver)
        return ck




