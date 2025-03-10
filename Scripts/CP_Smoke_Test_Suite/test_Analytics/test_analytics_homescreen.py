import pytest

from TestData.CP_Test_Data import loginData
from Utilities.BaseClass import BaseClass


class TestAnalyticsScreen(BaseClass):

    @pytest.mark.smoke
    def test_verify_analytics_home_screen(self, ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.navigate_to_module('Analytics')
        ui.analytics.verify_analytics_page()
