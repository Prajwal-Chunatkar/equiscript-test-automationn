import pytest

from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from TestData.CP_Test_Data import loginData
from Utilities.BaseClass import BaseClass


class TestConfiguration(BaseClass):

    @pytest.mark.smoke
    def test_verify_CE_screen(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        login_page.switchto_homepage()
        home_page.navigate_to_module('Configuration')
        home_page.verify_ce_page()