import time

import pytest

from PageObjects.ConfigurationMangementModule.CoveredEntity.Covered_Entity import CoveredEntity
from PageObjects.LoginPage import LoginPage
from PageObjects.UserManagementModule.UserManagement.User_Management import UserManagement
from TestData.CP_Test_Data import loginData
from Utilities.BaseClass import BaseClass

rnd = str(int(round(time.time())))


class Test_Table_Handling(BaseClass):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.user_login(loginData.username, loginData.password)

    def test_verify_export_button(self):
        covered_entity = CoveredEntity(self.driver)
        user_management = UserManagement(self.driver)
        self.verify_element_present(user_management.USER_MANAGEMENT_TAB, 20)
        self.click_element(user_management.USER_MANAGEMENT_TAB)
        time.sleep(5)
        self.click_element(covered_entity.EXPORT_BUTTON)
        time.sleep(5)
        # self.file_rename("Rajesh" + str(rnd) + ".csv", "D:\\PythonDemo\\DownloadFiles")
        # csvFile1 = pandas.read_csv(os.getcwd() + f'\\DownloadFiles\\{rnd}.csv')

    def test_verify_table_dropdowns(self):
        user_management = UserManagement(self.driver)
        user_management.um_table_page_nation_dropdowns()

    def test_verify_table_page_nations(self):
        user_management = UserManagement(self.driver)
        user_management.um_table_page_nations()
