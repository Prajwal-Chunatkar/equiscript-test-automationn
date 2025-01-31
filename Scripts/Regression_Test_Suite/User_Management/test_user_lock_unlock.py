import time
import pytest
from Utilities.BaseClass import BaseClass
from PageObjects.LoginPage import LoginPage
from PageObjects.UserManagementModule.UserManagement.User_Management import UserManagement
from TestData.CP_Test_Data import loginData, userManagement, resetPassword, emailNotification

rnd = str(int(round(time.time())))
email = 'testlockuser' + rnd + '@mailinator.com'
user_name = 'testlockuser' + rnd


# email = "testlockuser1686816077@mailinator.com"
# user_name = "testlockuser1686816077"


class TestUserLockUnLock(BaseClass):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.user_login(loginData.username, loginData.password)

    def test_add_lock_user(self):
        login_page = LoginPage(self.driver)
        user_management = UserManagement(self.driver)
        # login_page.user_login(loginData.username, loginData.password)
        user_management.add_user(userManagement.super_admin, "firstnametest",
                                 "lastnametest", email, resetPassword.favourite_destination,
                                 resetPassword.born_city, 'Hyderabad', "Hyderabad", "Password!1")
        login_page.user_login(email, "Password!1")
        login_page.user_logout()

    def test_one_unsuccessful_login_attempt(self):
        login_page = LoginPage(self.driver)
        user_management = UserManagement(self.driver)
        login_page.user_lock_login(email, "Password11")
        self.verify_element_present(login_page.INCORRECT_LOGIN_DETAILS, 10)
        incorrect_login_attempts = self.get_text(login_page.INCORRECT_LOGIN_DETAILS)
        assert incorrect_login_attempts == userManagement.validation_message_after_invalid_login
        number_of_attempts = self.get_text(login_page.NUMBER_OF_LOGIN_ATTEMPTS_TWO)
        assert number_of_attempts == "Remaining attempts: 2"
        time.sleep(5)

    def test_two_unsuccessful_login_attempts(self):
        login_page = LoginPage(self.driver)
        user_management = UserManagement(self.driver)
        login_page.user_lock_login(email, "Password12")
        self.verify_element_present(login_page.INCORRECT_LOGIN_DETAILS, 10)
        incorrect_login_attempts = self.get_text(login_page.INCORRECT_LOGIN_DETAILS)
        assert incorrect_login_attempts == userManagement.validation_message_after_invalid_login
        number_of_attempts = self.get_text(login_page.NUMBER_OF_LOGIN_ATTEMPTS_ONE)
        assert number_of_attempts == "Remaining attempt: 1"
        time.sleep(5)

    def test_three_unsuccessful_login_attempts(self):
        login_page = LoginPage(self.driver)
        user_management = UserManagement(self.driver)
        login_page.user_lock_login(email, "Password12")
        self.verify_element_present(login_page.LOGIN_ATTEMPT_FAILED, 10)
        incorrect_login_attempts = self.get_text(login_page.LOGIN_ATTEMPT_FAILED)
        assert incorrect_login_attempts == userManagement.validation_message_after_3rd_time_login
        number_of_attempts = self.get_text(login_page.REGISTRATION_LINK_SENT_TO_EMAIL)
        assert number_of_attempts == userManagement.validation_message_when_user_lock
        time.sleep(2)
        user_management.unlock_user(email, "Hyderabad", "Hyderabad", "Password!2", emailNotification.app_locked_sub)
        self.get_url(loginData.url)
        time.sleep(2)
        login_page.user_login(email, "Password!2")
        time.sleep(5)
