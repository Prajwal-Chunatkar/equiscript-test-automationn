from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass

class Endpoints(object):

    DASHBOARD = (By.XPATH, "//li//span[text()='Dashboard']")
    CONFIGURATION_MANAGEMENT = (By.XPATH, "//span[text()='Configuration']")
    USER_MANAGEMENT = (By.XPATH, "//span[text()='User Management']")
    PATIENT_MANAGEMENT = (By.XPATH, "//span[text()='Patient Management']")
    CLAIMS_MANAGEMENT = (By.XPATH, "//span[text()='Claims Management']")
    INVENTORY_MANAGEMENT = (By.XPATH, "//span[text()='Inventory Management']")
    ORDER_MANAGEMENT = (By.XPATH, "//span[text()='Order Management']")
    BILLING_MANAGEMENT = (By.XPATH, "//span[text()='Billing Management']")
    COVERED_ENTITY = (By.XPATH, "//span[text()='Covered Entity']")
    CHAINS = (By.XPATH, "//span[text()='Chains']")
    PHARMACIES = (By.XPATH, "//span[text()='Pharmacies']")

    ##configuration
class Configuration(object):

    COVERED_ENTITIES = (By.XPATH,"//span[text()='Covered Entities']")
    ADD_COVERED_ENTITY = (By.XPATH,"//span[text()=' Add Covered Entity']")
    COVERED_ENTITY_NAME = (By.XPATH,"//span[text()='Covered Entity Name']")
    EXPORT = (By.XPATH,"//span[text()=' Export']")

class Claims(object):
    ADD_SEARCH = (By.XPATH,"//span[text()=' Add Search Criteria']")
    CLAIMS_MANAGEMENT = "//span[text()='Claims Management']"
    FIELD_NAME = (By.XPATH,"//span[text()='Field Name']")
    OPERATOR = (By.XPATH,"//span[text()='Operator']")
    VALUE = (By.XPATH,"//span[text()='Operator']")


class HomePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver


    def dashboard_elements(self):
        # self.verify_element_present(self.DASHBOARD, 30)
        checklist = [self.element_visible(Endpoints.DASHBOARD),
                     self.element_visible(Endpoints.CONFIGURATION_MANAGEMENT),
                     self.element_visible(Endpoints.USER_MANAGEMENT),
                     self.element_visible(Endpoints.PATIENT_MANAGEMENT),
                     self.element_visible(Endpoints.CLAIMS_MANAGEMENT),
                     self.element_visible(Endpoints.INVENTORY_MANAGEMENT),
                     self.element_visible(Endpoints.ORDER_MANAGEMENT),
                     self.element_visible(Endpoints.BILLING_MANAGEMENT), self.element_visible(Endpoints.COVERED_ENTITY),
                     self.element_visible(Endpoints.CHAINS), self.element_visible(Endpoints.PHARMACIES)]
        assert not (False in checklist)," element not present on Dashboard screen"

    def navigate_to_module(self,module):
        self.click_element_by_moduleName('Dashboard')
        self.click_element_by_moduleName(module)

    def verify_ce_page(self):
        checklist = [self.element_visible(Configuration.COVERED_ENTITIES),
                     self.element_visible(Configuration.ADD_COVERED_ENTITY),
                     self.element_visible(Configuration.COVERED_ENTITY_NAME),
                     self.element_visible(Configuration.EXPORT)]
        assert not (False in checklist), " element not present on Covered Entity screen"

    # def verify_claims_management_page(self):
    #     elements = self.get_webelements(Claims.CLAIMS_MANAGEMENT)
    #     checklist = ['claims' in self.driver.current_url, len(elements) > 1,
    #                  self.element_visible(Claims.ADD_SEARCH)]
    #     assert not (False in checklist), " element not present on Claim Management screen"

    def add_search_crieteria(self):
        self.click_element(Claims.ADD_SEARCH)
        checklist = [self.element_visible(Claims.FIELD_NAME), self.element_visible(Claims.OPERATOR),
                     self.element_visible(Claims.VALUE)]
        assert not (False in checklist), " element not present on add search crieteria screen"







