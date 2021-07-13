import logging
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utilities import custon_logging as cl

class BaseMethodDrivers:
    log = cl.loggingtest(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatortype):
        """
        get the By Type of the locatortype
        #ghlk
        #hkop
        """


        try:
            locatortype= locatortype.lower()
            if locatortype == "id":
                return By.ID
            elif locatortype == "xpath":
                return By.XPATH
            elif locatortype == "css":
                return By.CSS_SELECTOR
            elif locatortype == "name":
                return By.NAME
            elif locatortype == "link":
                return By.LINK_TEXT
            elif locatortype == "class":
                return By.CLASS_NAME
            self.log.info("locatortype "+locatortype + " has been returned")
        except:
            self.log.error("locatortype " + locatortype + " has NOT been returned")

    def getelement(self, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            byType = self.getByType(locatortype)
            element = self.driver.find_element(byType,locator)
            self.log.info("Element with locator "+locator +" and locatortype "+locatortype +" has been returned")
            return element
        except:
            self.log.error("Element with locator "+locator +" and locatortype "+locatortype +" has NOT been returned")

    def getelementlist(self, locator, locatortype="id"):
        try:
            locatortype= locatortype.lower()
            byType = self.getByType(locatortype)
            elementlist = self.driver.find_elements(byType, locator)
            self.log.info("Elementlist with locator " + locator + " and locatortype " + locatortype + " has been returned")
            return elementlist
        except:
            self.log.error("Elementlist with locator " + locator + " and locatortype " + locatortype + " has NOT been returned")

    def clickelement(self, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            element = self.getelement(locator, locatortype)
            element.click()
            self.log.info("Element with locator "+locator +" and locatortype "+locatortype +" has been clicked")
        except:
            self.log.error("Element with locator " + locator + " and locatortype " + locatortype + " has NOT been clicked")

    def senddata(self, data, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            element = self.getelement(locator, locatortype)
            element.send_keys(data)
            self.log.info("Data " +str(data) + " sent to Element with locator "+locator +" and locatortype "+locatortype)
        except:
            self.log.error("Data " + str(data) + " NOT sent to Element with locator " + locator + " and locatortype " + locatortype)


    def verifypresence(self, locator, locatortype="id"):

            locatortype= locatortype.lower()
            elementlist = self.getelementlist(locator, locatortype)
            if len(elementlist) > 0:
                self.log.info("Element with locator "+locator +" and locatortype "+locatortype + " is present")
                return True
            else:
                self.log.info("Element with locator "+locator +" and locatortype "+locatortype + " is NOT present")
                return False


    def dropdownvisibletext(self, text, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            select = Select(self.getelement(locator,locatortype))
            select.select_by_visible_text(text)
            self.log.info("visible text "+text + " selected from the dropdown with locator "+locator + " and locatortype " +locatortype )
        except:
            self.log.error("visible text " + text + "NOT selected from the dropdown with locator " + locator + " and locatortype " +locatortype)


    def waitforpresence(self, waittime, locator,locatortype ="id"):
        try:
            locatortype= locatortype.lower()
            wait = WebDriverWait(self.driver, waittime)
            wait.until(expected_conditions.presence_of_element_located((locatortype, locator)))
            self.log.info("waiting for presence of element with locator "+locator +" and locatortype "+locatortype)
        except:
            self.log.error("Issue in wait for presence of element with locator "+locator +" and locatortype "+locatortype)

    def waitforelementclickable(self, waittime, locator, locatortype="id"):
        element = None
        try:
            locatortype = locatortype.lower()
            wait = WebDriverWait(self.driver, waittime)
            element=wait.until(expected_conditions.element_to_be_clickable((locatortype, locator)))
            self.log.info("waiting for element to be clickable with locator " + locator + " and locatortype " + locatortype)
        except:
            self.log.error("Issue in waiting for element to be clickable for presence of element with locator " + locator + " and locatortype " + locatortype)
        return element

    def switchframe(self, locator, locatortype="id"):
        try:
            locatortype= locatortype.lower()
            self.driver.switch_to.frame(self.getelement(locator, locatortype))
            self.log.info("switching to frame with locator "+locator + " and locatortype "+locatortype)
        except:
            self.log.error("error in switching to frame with locator "+locator + " and locatortype "+locatortype)

    def switchwindow(self, winnumber):
        try:
            self.driver.switch_to.window(self.driver.window_handles[winnumber])
            self.log.info("switched to window with number "+winnumber)
        except:
            self.log.error("error in switching to window with number "+winnumber)

    def textinalert(self):
        try:
            alert=self.driver.switch_to.alert
            alerttext = alert.text
            self.log.info("text in the alert is returned "+alerttext)
            return alerttext
        except:
            self.log.error("Error in returning text from alert")

    def webscroll(self, direction):
        try:
            direction = direction.lower()
            if direction == "up":
                self.driver.execute_script("window.scroll(0,-1000);")
                self.log.info("Scrolled Up")
            elif direction == "down":
                self.driver.execute_script("window.scroll(0,1000);")
                self.log.info("scrolled down")
        except:
            self.log.error("issue in scrolling")

    def scrollinview(self, locator, locatortype):
        try:
            locatortype= locatortype.lower()
            element = self.getelement(locator, locatortype)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.log.info("scrolled in view for element with locator "+locator + " and locatortype "+locatortype)

        except:
            self.log.error("issue with scrolling in view for element with locator "+locator + " and locatortype "+locatortype)

    def getText(self,locator,locatortype="id"):
        locatortype= locatortype.lower()
        element = self.getelement(locator, locatortype)
        if element is not None:
            text = element.text
            self.log.info("text "+ text +" returned from element with locator "+locator +" and locatortype "+locatortype)
            return text
        else:
            self.log.error("no text returned from element with locator "+locator +" and locatortype "+locatortype)


    def getScreenshot(self, resultmessage):
        filename = resultmessage+ str(time.time()*1000)+ ".png"
        screenshotdirectory = "../Screenshots/"
        relativefilename = screenshotdirectory+filename
        currentdirectory = os.path.dirname(__file__)
        destinationfilename = os.path.join(currentdirectory, relativefilename)
        destinationdirectory = os.path.join(currentdirectory, screenshotdirectory)

        try:
            if not os.path.exists(destinationdirectory):
                os.makedirs(destinationdirectory)

            self.driver.save_screenshot(destinationfilename)
            self.log.info("screenshot " +destinationfilename+" saved in directory "+destinationdirectory)
        except:
            self.log.error("error in saving screenshot")


    def clickradioonvalue(self, locator,ovalue,locatortype= "id"):
        locatortype = locatortype.lower()
        elementlist = self.getelementlist(locator, locatortype)
        self.log.info("length of element list is " +str(len(elementlist)))

        for element in elementlist:
            if element.get_attribute('value')== ovalue:
                element.click()

                self.log.info("Element with locator "+locator +" and locatortype "+locatortype +" and value "+ovalue+ "is clicked")
                break
            else:
                self.log.error("Element with locator " + locator + " and locatortype " + locatortype + " and value " + ovalue + "is NOT clicked")


    def clickallradio(self, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            elementlist = self.getelementlist(locator, locatortype)

            for element in elementlist:
                element.click()
                time.sleep(5)
            self.log.info("All elements with locator "+locator + " and locatortype "+locatortype +" clicked")
        except:
            self.log.error("All elements with locator "+locator + " and locatortype "+locatortype +" NOT clicked")

    def checkenabled(self, locator, locatortype="id"):
        try:
            locatortype =locatortype.lower()
            element = self.getelement(locator, locatortype)
            if element.is_enabled is True:
                self.log.info("Element with locator "+locator +" and locatortype "+locatortype +" is enabled")
                return True
            else:
                self.log.info("Element with locator " + locator + " and locatortype " + locatortype + " is disabled")
                return False
        except:
            self.log.error("Issue with element while checking enabled or disabled")

    def getxpathfromchild(self,childt,locator):
        try:
            byType= self.getByType("xpath")
            xpa= childt.find_element(byType, locator)
            self.log.info("Xpath of child "+locator +" is returned ")
            return xpa
        except:
            self.log.error("xpath of locator "+locator + " is not returned")