import time
from PageObjects.LoginPage import LoginPage
from PageObjects.ConfigurationMangementModule.CoveredEntity.Covered_Entity import CoveredEntity
from TestData.CP_Test_Data import loginData
from Utilities.BaseClass import BaseClass


class Test_Table_Handling(BaseClass):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.user_login(loginData.username, loginData.password)

    def test_verify_export_button(self):
        covered_entity = CoveredEntity(self.driver)
        self.verify_element_present(covered_entity.CONFIGURATION_MANAGEMENT, 20)
        self.click_element(covered_entity.CONFIGURATION_MANAGEMENT)
        time.sleep(5)
        self.click_element(covered_entity.EXPORT_BUTTON)
        time.sleep(2)

    def test_verify_table_dropdowns(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.cf_table_page_nation_dropdowns()

    def test_verify_table_page_nations(self):
        login_page = LoginPage(self.driver)
        covered_entity = CoveredEntity(self.driver)
        covered_entity.cf_table_page_nations()
        login_page.user_logout()

