import time
import pytest
from TestData.CP_Test_Data import loginData, resetPassword, userManagement
from Utilities.BaseClass import BaseClass
from PageObjects.LoginPage import LoginPage
from PageObjects.UserManagementModule.UserManagement.User_Management import UserManagement
from PageObjects.ConfigurationMangementModule.CoveredEntity.Covered_Entity import CoveredEntity
from PageObjects.HomePage import HomePage

rnd = str(int(round(time.time())))
email = 'testsmokeuser' + rnd + '@mailinator.com'
user_name = 'testsmokeuser' + rnd

@pytest.mark.usefixtures('setup')
class Test_Smoke_CP(BaseClass):


    @pytest.mark.run(order=1)
    def test_login(self,setup):
        login_page = LoginPage(self.driver)
        login_page.user_login(loginData.username, loginData.password)

    @pytest.mark.run(order=2)
    @pytest.mark.depends(on=['test_login'])
    def test_verify_left_side_menu(self):
        home_page = HomePage(self.driver)
        home_page.left_side_menu()

    @pytest.mark.run(order=3)
    @pytest.mark.depends(on=['test_login'])
    def test_navigate_to_add_user_page(self):
        user_management = UserManagement(self.driver)
        user_management.user_navigation()

    @pytest.mark.run(order=4)
    @pytest.mark.depends(on=['test_login'])
    def test_add_new_user(self):
        login_page = LoginPage(self.driver)
        user_management = UserManagement(self.driver)
        user_management.add_user(userManagement.super_admin, "firstnametest",
                                 "lastnametest", email, resetPassword.favourite_destination,
                                 resetPassword.born_city, 'Hyderabad', "Hyderabad", "Password!1")
        login_page.user_login(email, "Password!1")
        login_page.user_logout()

    @pytest.mark.run(order=5)
    @pytest.mark.depends(on=['test_login'])
    def test_verify_view_option_in_user_management_table(self):
        login_page = LoginPage(self.driver)
        user_management = UserManagement(self.driver)
        login_page.user_login(loginData.username, loginData.password)
        self.verify_element_present(user_management.USER_MANAGEMENT_TAB, 20)
        self.click_element(user_management.USER_MANAGEMENT_TAB)
        self.verify_element_present(user_management.VIEW_OPTION, 20)
        assert self.element_visible(user_management.VIEW_OPTION) == True

    @pytest.mark.run(order=6)
    @pytest.mark.depends(on=['test_login'])
    def test_verify_edit_option_in_user_management_table(self):
        user_management = UserManagement(self.driver)
        user_management.verify_edit_button_in_table()

    @pytest.mark.run(order=7)
    @pytest.mark.depends(on=['test_login'])
    def test_navigate_to_ce_page(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.verify_add_ce_page()

    @pytest.mark.run(order=8)
    @pytest.mark.depends(on=['test_login'])
    def test_navigate_to_pharmacies_page(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.navigate_to_pharmacies()
        time.sleep(10)

    @pytest.mark.run(order=9)
    @pytest.mark.depends(on=['test_login'])
    def test_add_new_covered_entity(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.add_new_covered_entity("OPAID" + rnd, "CE" + rnd, "Critical Access Hospitals (CAH)",
                                              "Npicode" + rnd, "pharmacyName" + rnd, "Nabpcode" + rnd,
                                              "In-House Pharmacy", rnd, "Hyderabad", "Cardinal", rnd)

    @pytest.mark.run(order=10)
    @pytest.mark.depends(on=['test_login'])
    def test_verify_view_button_in_ce_table(self):
        covered_entity = CoveredEntity(self.driver)
        covered_entity.verify_view_button_in_grid("OPAID" + rnd)
        time.sleep(10)

    @pytest.mark.run(order=11)
    @pytest.mark.depends(on=['test_login'] and ['test_verify_view_button_in_ce_table'])
    def test_verify_eligibility_rule_admin_fee_tabs(self):
        login_page = LoginPage(self.driver)
        covered_entity = CoveredEntity(self.driver)
        self.verify_element_present(covered_entity.ELIGIBILITY_RULE, 20)
        assert self.element_visible(covered_entity.ELIGIBILITY_RULE) == True
        assert self.element_visible(covered_entity.ADMIN_FEE) == True
        login_page.user_logout()
