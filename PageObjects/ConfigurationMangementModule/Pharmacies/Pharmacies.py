from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass
from PageObjects.ConfigurationMangementModule.CoveredEntity.Covered_Entity import CoveredEntity
from PageObjects.LoginPage import LoginPage


class Pharmacies(BaseClass):
    def __init__(self, driver):
        self.driver = driver

        ADD_PHARMACY_BUTTON = (By.XPATH, "//span[contains(text(), 'Add Pharmacy')]")

    def search_new_pharmacy(self,pharmacy, storeNum, npi, nabp):
        log = self.get_logger()
        covered_entity = CoveredEntity(self.driver)
        self.verify_element_present(covered_entity.CONFIGURATION_MANAGEMENT, 10)
        self.click_element(covered_entity.CONFIGURATION_MANAGEMENT)
        self.move_to_Element(covered_entity.SELECT_ENTITY_TYPE)
        self.verify_element_present(covered_entity.SELECT_PHARMACY_PAGE, 10)
        self.click_element(covered_entity.SELECT_PHARMACY_PAGE)
        self.verify_element_present(covered_entity.ADD_PHARMACY_BUTTON, 30)
        self.send_Keys(covered_entity.SEARCH_HERE, pharmacy)
        self.search_user(LoginPage.TOTAL_ROWS, 1, 1, LoginPage.SINGLE_ROW, LoginPage.SINGLE_COLUMN, pharmacy,
                         storeNum,npi,nabp, "Pharmacies","")
