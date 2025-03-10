import pytest

from TestData.CP_Test_Data import loginData
from Utilities.BaseClass import BaseClass


class TestOrderManagement:

    @pytest.mark.smoke
    def test_verify_order_management_screen(self, ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Order Management')
        ui.ordermanagement.validate_order_management_page()
        ui.ordermanagement.validate_searchfilter()

    @pytest.mark.smoke
    def test_verify_add_search_criteria_screen(self,ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Order Management')
        ui.ordermanagement.validate_order_management_page()
        ui.ordermanagement.validate_searchfilter()
        ui.ordermanagement.validate_add_search_crieteria()

    @pytest.mark.smoke
    def test_verify_covered_entity_details_screen(self, ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Order Management')
        ui.ordermanagement.validate_order_management_page()
        ui.ordermanagement.validate_searchfilter()
        ui.ordermanagement.validate_add_search_crieteria()
        ui.ordermanagement.select_data_for_orders_and_validate()

    @pytest.mark.smoke
    def test_verify_order_details_screen(self,ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Order Management')
        ui.ordermanagement.validate_order_management_page()
        ui.ordermanagement.validate_searchfilter()
        ui.ordermanagement.validate_add_search_crieteria()
        ui.ordermanagement.select_data_for_orders_and_validate()
        ui.ordermanagement.validate_PO_details_screen()

if __name__=="__main__":
    print("Test case execution done")