from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass


class HomePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    DASHBOARD = (By.XPATH, "//span[text()='Dashboard']")
    CONFIGURATION_MANAGEMENT = (By.XPATH, "//span[text()='Configuration Management']")
    USER_MANAGEMENT = (By.XPATH, "//span[text()='User Management']")

    def left_side_menu(self):
        self.verify_element_present(self.DASHBOARD, 30)
        dashboard_status = self.element_visible(self.DASHBOARD)
        assert dashboard_status == True
        cm_status = self.element_visible(self.CONFIGURATION_MANAGEMENT)
        assert cm_status == True
        um_status = self.element_visible(self.USER_MANAGEMENT)
        assert um_status == True
