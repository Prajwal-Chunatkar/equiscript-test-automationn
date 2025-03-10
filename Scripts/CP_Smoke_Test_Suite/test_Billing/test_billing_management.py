import pytest

from TestData.CP_Test_Data import loginData
from Utilities.BaseClass import BaseClass


class TestBillingManagement(BaseClass):

    @pytest.mark.smoke
    def test_verify_billing_management_screen(self, ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Billing Management')
        ui.billing.verify_billing_management_page()