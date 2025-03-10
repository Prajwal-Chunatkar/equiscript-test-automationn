import random
import time
import pytest

from TestData.CP_Test_Data import loginData, resetPassword, userManagement
from Utilities.BaseClass import BaseClass

# rnd = str(int(round(time.time())))
# email = 'testsmokeuser' + rnd + '@mailinator.com'

email = 'testsmokeuser'+str(random.randint(100, 999))+'@mailinator.com'
# user_name = 'testsmokeuser' + rnd


class TestSmokeCP(BaseClass):


    # @pytest.mark.smoke
    # def test_login(self,ui):
    #     ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
    #     ui.login_page.switchto_homepage()

    @pytest.mark.smoke
    def test_verify_dashboard_screen(self,ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        ui.home_page.dashboard_elements()

    @pytest.mark.smoke
    def test_navigate_to_add_user_page(self,ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage)(
        ui.user_management.user_navigation()

    @pytest.mark.smoke
    def test_add_superadmin_user(self,ui):
        # ui.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        # ui.login_page.switchto_homepage()
        username = ui.user_management.add_user(userManagement.super_admin, "firstnametest",
                                 "lastnametest", email, resetPassword.favourite_destination,
                                 resetPassword.born_city, 'Hyderabad', "Hyderabad", "Password!1")
        ui.login_page.newuser_login_and_logout(username, "Password!1", email)




if __name__=="__main__":
    print("Executed when invoked directly")