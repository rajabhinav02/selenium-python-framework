import pytest

from Pages.Homepage.Homepage import homepage
from Utilities.TestStatus import testStatus

@pytest.mark.usefixtures("setup")
class TestShop:

    @pytest.fixture(autouse=True)
    def classsetup(self):
        self.hm = homepage(self.driver)
        self.ts = testStatus(self.driver)

    @pytest.mark.p
    def test_form(self,formdata):
        dis = self.hm.verifyentredisabled()
        self.ts.marktest(dis, "Enterp is disabled")
        self.hm.submitform(formdata["First_Name"], formdata["email"], formdata["Password"], formdata["Gender"],formdata["Date"], formdata["Month"], formdata["Year"])
        msg=self.hm.verifySuccess()
        self.ts.marktestfinal(msg,"Form Submission", "test_form")

    def test_shop(self, shopdata):
        self.bp = self.hm.clickShop()
        self.bp.clickadd(shopdata["Brand_Name"])
        self.ck = self.bp.clickcheckout()
        brandna=self.ck.validatebrand(shopdata["Brand_Name"])
        self.ts.marktest(brandna, "Brand Name selected")
        amountse=self.ck.validateselectedamount()
        self.ts.marktest(amountse,"Amount Selected")
        self.cn = self.ck.clickCheckoutagain()
        self.cn.submitorder(shopdata["Country"], shopdata["Country_Name"])
        orders= self.cn.validateordersuccess()
        self.ts.marktestfinal(orders,"Order Submitted", "test_shop")



