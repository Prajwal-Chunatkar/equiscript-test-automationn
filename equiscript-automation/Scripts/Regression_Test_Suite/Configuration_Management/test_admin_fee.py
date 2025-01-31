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
tomorrow_date = (x + datetime.timedelta(1)).strftime('%m/%d/%Y')
next_date_of_tomorrow = (x + datetime.timedelta(2)).strftime('%m/%d/%Y')

# opa_id = "OPAID_AF" + rnd
# new_ce = "CE_AF" + rnd


opa_id = "OPAID_AF1688649963"

new_ce = "CE_AF1688649963"


class Test_Verify_Admin_fee(BaseClass):

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.user_login(loginData.username, loginData.password)

    def test_view_ce_user(self):
        covered_entity = CoveredEntity(self.driver)
        # covered_entity.add_new_covered_entity(opa_id, new_ce, "Free-Standing Cancer Hospitals (CAN)",
        #                                       "AFNpicode" + rnd, "AFPharmacy" + rnd, "AFNabpcode" + rnd,
        #                                       "Contracted Retail Pharmacy", rnd, "Hyderabad", "AmerisourceBergen",
        #                                       "AC_AF" + rnd)
        covered_entity.ce_view_user(new_ce, opa_id, "0", "0", "Pending")

    #
    def test_add_term_date_live_date_for_ce(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.eligibility_rule(current_date, future_date, "Update Live Date & Term Date",
                                        "Live date and Term date updated successfully.")
        covered_entity.patient_eligibility_term_date(1, "Patient Eligibility Term Date saved successfully",
                                                     "AddPatientEligibility")
        time.sleep(2)
        covered_entity.ce_view_user(new_ce, opa_id, "0", "0", "Active")

    def test_admin_fee(self):
        covered_entity = CoveredEntity(self.driver)
        print(tomorrow_date)
        covered_entity.add_admin_fee(tomorrow_date, "Percentage of Net", 1, new_ce, "")
        time.sleep(5)

    def test_add_new_admin_fee(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.add_admin_fee(next_date_of_tomorrow, "Flat Fee", 2, new_ce, "add")
        # time.sleep(5)
