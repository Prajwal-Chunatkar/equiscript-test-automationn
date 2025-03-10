import pytest

from TestData.CP_Test_Data import loginData
from Utilities.BaseClass import BaseClass

class TestClaimsManagement(BaseClass):



    @pytest.mark.smoke
    def test_verify_claims_management_screen(self,ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Claims Management')
        ui.claims.verify_claims_management_page()

    @pytest.mark.smoke
    def test_verify_add_search_criteria_screen(self,ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Claims Management')
        ui.claims.add_search_crieteria()

    @pytest.mark.smoke
    def test_verify_covered_entity_details_screen(self,ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Claims Management')
        ui.claims.add_search_crieteria()
        ui.claims.select_data_for_claim_and_validate("AltaMed Health Services Corporation")


    @pytest.mark.smoke
    def test_verify_non_captured_status_and_claim_saving(self, ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Claims Management')
        ui.claims.add_search_crieteria()
        ui.claims.select_data_for_claim_and_validate("AltaMed Health Services Corporation")
        ui.claims.verify_capture_non_captured()
        ui.claims.verify_claim_saving_opportunity()
        ui.claims.verify_claim_status()

if __name__=="__main__":
    print("Test case execution done")


