import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestInventoryManagement:

    # @pytest.mark.smoke
    # def test_url_loading(self):
    #     service = Service(
    #         "C:\\Users\\Prajwal.Chunatkar\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
    #     # driver = webdriver.Chrome(service=service,options=options)
    #     driver = webdriver.Chrome(service=service)
    #     driver.get("https://qa.equiscript.com/login")

    @pytest.mark.smoke
    def test_verify_inventory_screen(self, ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Inventory Management')
        ui.inventory_management.validate_inventory_management_page()

    @pytest.mark.smoke
    def test_verify_inventory_data_table(self, ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Inventory Management')
        ui.inventory_management.validate_inventory_management_page()
        ui.inventory_management.add_search_crieteria()
        ui.inventory_management.select_data_for_inventory_and_validate("Moon River Health, Inc.")

    @pytest.mark.smoke
    def test_verify_Dispensed_Qty_and_Rx_DetailsScreen(self, ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Inventory Management')
        ui.inventory_management.validate_inventory_management_page()
        ui.inventory_management.add_search_crieteria()
        ui.inventory_management.select_data_for_inventory_and_validate("Moon River Health, Inc.")
        ui.inventory_management.validate_navigation_to_dispense_qty_info()
        ui.inventory_management.validate_navigation_to_rx_details_screen()

    @pytest.mark.smoke
    def test_verify_Dispensed_Qty_and_PO_DetailsScreen(self, ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Inventory Management')
        ui.inventory_management.validate_inventory_management_page()
        ui.inventory_management.add_search_crieteria()
        ui.inventory_management.select_data_for_inventory_and_validate("Moon River Health, Inc.")
        ui.inventory_management.validate_navigation_to_dispense_qty_info()
        ui.inventory_management.validate_navigation_to_PO_details_screen()

if __name__=="__main__":
    print("test execution")


