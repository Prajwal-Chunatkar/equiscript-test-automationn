import datetime
import time

from PageObjects.LoginPage import LoginPage
from TestData.CP_Test_Data import loginData
from Utilities.BaseClass import BaseClass
from PageObjects.ConfigurationMangementModule.CoveredEntity.Covered_Entity import CoveredEntity

rnd = str(int(round(time.time())))
x = datetime.datetime.now()
future_date = str(x.strftime("%m")) + "/" + str(x.strftime("%d")) + "/" + str(x.year + 1)
current_date = str(x.strftime("%m")) + "/" + str(x.strftime("%d")) + "/" + str(x.year)
opa_id = "OPAID_V" + rnd
ce = "CE_V" + rnd


class Test_CE_View_User(BaseClass):

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.user_login(loginData.username, loginData.password)

    def test_add_covered_entity(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.add_new_covered_entity(opa_id,ce, "Sole Community Hospitals (SCH)",
                                              "VNpicode" + rnd, "VPharmacy" + rnd, "VNabpcode" + rnd,
                                              "Covered Entity Owned Pharmacy", rnd, "Hyderabad", "Cardinal", "AC_V"+rnd)

    def test_view_ce(self):
        covered_entity = CoveredEntity(self.driver)
        login_page = LoginPage(self.driver)
        covered_entity.ce_view_user(ce, opa_id, "0", "0", "Pending")
        login_page.user_logout()
