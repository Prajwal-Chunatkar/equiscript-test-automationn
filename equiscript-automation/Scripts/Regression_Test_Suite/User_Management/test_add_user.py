import time

import pytest

from Utilities.BaseClass import BaseClass
from PageObjects.LoginPage import LoginPage
from PageObjects.UserManagementModule.UserManagement.User_Management import UserManagement
from TestData.CP_Test_Data import loginData, userManagement, resetPassword

rnd = str(int(round(time.time())))
# email = 'testnewuser' + rnd + '@mailinator.com'
# user_name = 'testnewuser' + rnd
email="testnewuser1686832454@mailinator.com"


class Test_New_Add_User(BaseClass):

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.user_login(loginData.username, loginData.password)

    def test_add_super_admin_user(self):
        login_page = LoginPage(self.driver)
        user_management = UserManagement(self.driver)
        # login_page.user_login(loginData.username, loginData.password)
        # user_management.add_user(userManagement.super_admin, "firstnametest",
        #                          "lastnametest", email, resetPassword.favourite_destination,
        #                          resetPassword.born_city, 'Hyderabad', "Hyderabad", "Password!1")
        # login_page.user_login(email, "Password!1")
        # login_page.user_logout()
        # login_page.user_login(loginData.username, loginData.password)
        user_management.search_new_user(email, email, userManagement.super_admin)
        login_page.user_logout()








