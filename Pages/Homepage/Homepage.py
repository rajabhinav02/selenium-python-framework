import logging
import time

from Base.BaseMetods import BaseMethodDrivers
from Pages.Brandpage.Brandpage import BrandPage
from Utilities import custon_logging as cl

class homepage(BaseMethodDrivers):
    log = cl.loggingtest(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    """
    LOCATORS
    """
    __firstname = "//input[contains(@class, 'form-control') and (@name='name')]"
    __email = "[name='email']"
    __password = "[type='password']"
    __icecream = "#exampleCheck1"
    __dropdown = "#exampleFormControlSelect1"
    __employed = "//input[@id= 'inlineRadio2']"
    __entreprenuer = "[id = 'inlineRadio3']"
    __radiobuttons = "[type='radio']"
    __date = "[name='bday']"
    __submit = "[type='Submit']"
    __shop = "Shop" #link
    __successmessage= "//div[contains(@class,'alert-success')]//strong"

    def nameupdate(self, name):
        self.senddata(name,self.__firstname,"xpath")
    def emailupdate(self, email):
        self.senddata(email,homepage.__email,"css")
    def pwdupdate(self, pwd):
        self.senddata(pwd,self.__password,"css")
    def clickicecheck(self):
        self.clickelement(self.__icecream, "css")
    def selectgender(self, gendervalue):
        self.dropdownvisibletext(gendervalue,self.__dropdown,"css")
    def clickEmployed(self):
        self.clickradioonvalue(self.__radiobuttons, "option2", "css")


    def clickallEmpstatus(self):
        self.clickallradio(self.__radiobuttons, "css")

    def verifypresenceofEntre(self):
        presence=self.verifypresence(self.__entreprenuer,"css")
        if presence == True:
            return True
        else:
            return False
    def verifyentredisabled(self):
        enabled= self.checkenabled(self.__entreprenuer, "css")
        if enabled == True:
            return False
        else:
            return True
    

    def updatedate(self,date):
        self.clickelement(self.__date, "css")
        self.senddata(date, self.__date, locatortype="css")

    def updatemonth(self,month):
        self.clickelement(self.__date, "css")
        self.senddata(month, self.__date,"css")

    def updateyear(self, year):
        self.clickelement(self.__date, "css")
        self.senddata(year,self.__date, "css")

    def clickSubmit(self):
        self.clickelement(self.__submit, "css")

    def verifySuccess(self):
        message=self.getText(self.__successmessage, "xpath")
        if "Success" in message:
            return True
        else:
            return False

    def submitform(self, name, email, pwd, gendervalue, date, month, year):
        self.nameupdate(name)
        self.emailupdate(email)
        self.pwdupdate(pwd)
        self.clickicecheck()
        self.selectgender(gendervalue)
        self.clickEmployed()
        self.clickallEmpstatus()
        self.updatedate(date)
        self.updatemonth(month)
        self.updateyear(year)
        self.clickSubmit()

    def clickShop(self):
        self.clickelement(self.__shop, "link")
        bp = BrandPage(self.driver)
        return bp


