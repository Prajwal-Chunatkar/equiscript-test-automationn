import time
import pytest
from Utilities.BaseClass import BaseClass
from PageObjects.LoginPage import LoginPage
from PageObjects.UserManagementModule.UserManagement.User_Management import UserManagement
from TestData.CP_Test_Data import loginData, userManagement, resetPassword, emailNotification

rnd = str(int(round(time.time())))
email = 'testforgotuser' + rnd + '@mailinator.com'
user_name = 'testforgotuser' + rnd


# email = "testforgotuser1686812330@mailinator.com"
# user_name = "testforgotuser1686812330"


class TestForgotUser(BaseClass):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.user_login(loginData.username, loginData.password)

    def test_add_forgot_user(self):
        login_page = LoginPage(self.driver)
        user_management = UserManagement(self.driver)
        # login_page.user_login(loginData.username, loginData.password)
        user_management.add_user(userManagement.super_admin, "firstnametest",
                                 "lastnametest", email, resetPassword.favourite_destination,
                                 resetPassword.born_city, 'Hyderabad', "Hyderabad", "Password!1")
        login_page.user_login(email, "Password!1")
        login_page.user_logout()

    def test_forgot_password(self):
        login_page = LoginPage(self.driver)
        user_management = UserManagement(self.driver)
        user_management.forgot_password(email)
        user_management.unlock_user(email, "Hyderabad", "Hyderabad", "Password!2",
                                    emailNotification.forgot_password_sub)
        self.get_url(loginData.url)
        time.sleep(2)
        login_page.user_login(email, "Password!2")
        time.sleep(5)
