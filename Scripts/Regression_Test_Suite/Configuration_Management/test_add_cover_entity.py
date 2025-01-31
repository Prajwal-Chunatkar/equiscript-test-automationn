import time
import datetime
from PageObjects.LoginPage import LoginPage
from TestData.CP_Test_Data import loginData
from Utilities.BaseClass import BaseClass
from PageObjects.ConfigurationMangementModule.CoveredEntity.Covered_Entity import CoveredEntity
from PageObjects.ConfigurationMangementModule.Pharmacies.Pharmacies import Pharmacies

rnd = str(int(round(time.time())))
x = datetime.datetime.now()
future_date = str(x.strftime("%m")) + "/" + str(x.strftime("%d")) + "/" + str(x.year + 1)
current_date = str(x.strftime("%m")) + "/" + str(x.strftime("%d")) + "/" + str(x.year)

ce_type = "Critical Access Hospitals (CAH)"
opa_id = "OPAID" + rnd
new_ce = "CE" + rnd


class Test_Add_Covered_Entity(BaseClass):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.user_login(loginData.username, loginData.password)

    def test_add_covered_entity(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.add_new_covered_entity(opa_id, new_ce, ce_type,
                                              "CENpicode" + rnd, "CEPharmacy" + rnd, "CENabpcode" + rnd,
                                              "In-House Pharmacy", rnd, "Hyderabad", "Cardinal", "CE_AC"+rnd)

    def test_verify_ce_in_table(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.search_new_covered_entity(opa_id, ce_type, "N/A", "N/A")

    def test_verify_pharmacy_in_table(self):
        pharmacies = Pharmacies(self.driver)
        pharmacies.search_new_pharmacy("CEPharmacy" + rnd, rnd, "CENpicode" + rnd, "CENabpcode" + rnd)

    def test_verify_accordian(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.verify_existing_opaid(opa_id)
        covered_entity.accordian("CENpicode" + rnd, "CENabpcode" + rnd, rnd, "In-House Pharmacy", "Hyderabad", "CE_AC"+rnd)
        # time.sleep(10)
