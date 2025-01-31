import time
import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.UserManagementModule.UserManagement.User_Management import UserManagement
from TestData.CP_Test_Data import loginData, userManagement, resetPassword
from Utilities.BaseClass import BaseClass


class Test_Add_Multiple_nUser(BaseClass):

    def test_login_users(self):
        login_page = LoginPage(self.driver)
        login_page.user_login(loginData.username, loginData.password)

    def test_add_super_admin_users(self):
        rnd = str(int(round(time.time())))
        email = 'testnewnuser' + rnd + '@mailinator.com'
        user_name = 'testnewnuser' + rnd
        login_page = LoginPage(self.driver)
        user_management = UserManagement(self.driver)
        user_management.add_user(userManagement.super_admin, "firstnametest",
                                 "lastnametest", email, resetPassword.favourite_destination,
                                 resetPassword.born_city, 'Hyderabad', "Hyderabad", "Password!1")
        login_page.user_login(email, "Password!1")
        login_page.user_logout()
        login_page.user_login(loginData.username, loginData.password)
        user_management.search_new_user(email, email, userManagement.super_admin)
        login_page.user_logout()

    def test_add_ce_users(self):
        rnd = str(int(round(time.time())))
        email = 'testnewceuser' + rnd + '@mailinator.com'
        user_name = 'testnewceuser' + rnd
        login_page = LoginPage(self.driver)
        user_management = UserManagement(self.driver)
        login_page.user_login(loginData.username, loginData.password)
        user_management.add_user(userManagement.ce_user, "firstnametest",
                                 "lastnametest", email, resetPassword.favourite_destination,
                                 resetPassword.born_city, 'Hyderabad', "Hyderabad", "Password!1")
        login_page.user_login(email, "Password!1")
        login_page.user_logout()
        login_page.user_login(loginData.username, loginData.password)
        user_management.search_new_user(email, email, userManagement.ce_user)
        login_page.user_logout()

    def test_add_pharma_users(self):
        rnd = str(int(round(time.time())))
        email = 'testnewpharmauser' + rnd + '@mailinator.com'
        user_name = 'testnewpharmauser' + rnd
        login_page = LoginPage(self.driver)
        user_management = UserManagement(self.driver)
        login_page.user_login(loginData.username, loginData.password)
        user_management.add_user(userManagement.pharmacy_user, "firstnametest",
                                 "lastnametest", email, resetPassword.favourite_destination,
                                 resetPassword.born_city, 'Hyderabad', "Hyderabad", "Password!1")
        login_page.user_login(email, "Password!1")
        login_page.user_logout()
        login_page.user_login(loginData.username, loginData.password)
        user_management.search_new_user(email, email, userManagement.pharmacy_user)
        login_page.user_logout()

    def test_add_standard_users(self):
        rnd = str(int(round(time.time())))
        email = 'testnewstandarduser' + rnd + '@mailinator.com'
        user_name = 'testnewstandarduser' + rnd
        login_page = LoginPage(self.driver)
        user_management = UserManagement(self.driver)
        login_page.user_login(loginData.username, loginData.password)
        user_management.add_user(userManagement.standard_user, "firstnametest",
                                 "lastnametest", email, resetPassword.favourite_destination,
                                 resetPassword.born_city, 'Hyderabad', "Hyderabad", "Password!1")
        login_page.user_login(email, "Password!1")
        login_page.user_logout()
        login_page.user_login(loginData.username, loginData.password)
        user_management.search_new_user(email, email, userManagement.standard_user)
        login_page.user_logout()

