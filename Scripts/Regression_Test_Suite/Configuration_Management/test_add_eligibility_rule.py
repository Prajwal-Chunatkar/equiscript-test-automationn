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
next_date = (x + datetime.timedelta(1)).strftime('%m/%d/%Y')



# opa_id = "OPAID_ER" + rnd
# new_ce = "CE_ER" + rnd


opa_id = "OPAID_AF1688640686"

new_ce = "CE_AF1688640686"


class Test_Verify_Eligibility_Rule(BaseClass):

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.user_login(loginData.username, loginData.password)

    def test_view_ce_user(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.add_new_covered_entity(opa_id, new_ce, "Disproportionate Share Hospitals (DSH)",
                                              "ERNpicode" + rnd, "ERPharmacy" + rnd, "ERNabpcode" + rnd,
                                              "Contracted Specialty Pharmacy", rnd, "Hyderabad", "McKesson", "AC_ER"+rnd)
        covered_entity.ce_view_user(new_ce, opa_id, "0", "0", "Pending")

    def test_add_term_date_live_date_for_ce(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.eligibility_rule(current_date, next_date, "Update Live Date & Term Date",
                                        "Live date and Term date updated successfully.")
        covered_entity.patient_eligibility_term_date(1, "Patient Eligibility Term Date saved successfully","AddPatientEligibility")
        time.sleep(2)
        covered_entity.ce_view_user(new_ce, opa_id, "0", "0", "Active")

    def test_updating_term_date(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.update_term_date(next_date)

    def test_update_patient_eligibility_rule(self):
        covered_entity = CoveredEntity(self.driver)
        self.click_element(covered_entity.RULE_2_EDIT_OPTION)
        covered_entity.patient_eligibility_term_date(5, "Patient Eligibility Term Date saved successfully","UpdatePatientEligibility")


