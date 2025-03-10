import pytest

from TestData.CP_Test_Data import loginData
from Utilities.BaseClass import BaseClass

class TestConfiguration(BaseClass):

    @pytest.mark.smoke
    def test_verify_CE_screen(self,ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Configuration')
        ui.home_page.verify_ce_page()

    # @pytest.mark.smoke
    # def test_verify_add_search_criteria_screen(self):
    #     login_page = LoginPage(self.driver)
    #     home_page = HomePage(self.driver)
    #     claim_page = ClaimManagement(self.driver)
    #     login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
    #     login_page.switchto_homepage()
    #     home_page.navigate_to_module('Claims Management')
    #     claim_page.add_search_crieteria()

if __name__=="__main__":
    print("Executed when invoked directly")
