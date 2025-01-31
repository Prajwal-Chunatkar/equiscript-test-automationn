import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass
from PageObjects.LoginPage import LoginPage


class CoveredEntity(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    # Cover Entities Page
    CONFIGURATION_MANAGEMENT = (By.XPATH, "//span[text()='Configuration Management']")
    ADD_CE_BUTTON = (By.XPATH, "//span[contains(text(),'Add Covered Entity')]")
    EXPORT_BUTTON = (By.XPATH, "//span[contains(text(), 'Export')]")
    OPA_ID_SEARCH = (
        By.XPATH, "//label[text()='OPA ID']/parent::div/following-sibling::div/descendant::div/button/span[text("
                  ")='Search']")
    CE_NAME_SEARCH = (By.XPATH,
                      "//label[text()='Covered Entity Name']/parent::div/following-sibling::div/descendant::div/button/span[text()='Search']")
    OPA_ID = (By.ID, "addce_opaid")
    CE_NAME = (By.ID, "addce_cename")
    CE_TYPE = (By.CLASS_NAME, "ant-select-selection-search")
    ADDRESS = (By.ID, "addce_address")
    CANCEL_BUTTON = (By.XPATH, "//span[text()='Cancel']")
    SAVE_BUTTON = (By.XPATH, "//span[text()='Save']")
    ADD_CONTINUE = (By.XPATH, "//span[text()='Add & Continue']")
    CONTINUE_BUTTON = (By.XPATH, "//span[text()='Continue']")
    NPI_CODE = (By.ID, "addpharmacy_npicode")
    PHARMACY_NAME = (By.ID, "addpharmacy_pharmacyname")
    NABP_CODE = (By.ID, "addpharmacy_nabpcode")
    PHARMACY_TYPE = (By.ID, "addpharmacy_pharmacytype")
    PHARMACY_STORE_NUMBER = (By.ID, "addpharmacy_pharmacystorenumber")
    SELECT_PHARMACY_WHOLESALER = (By.ID, "addpharmacy_wholesaler")
    WHOLESALER_ACCOUNT_NUMBER = (By.ID, "addpharmacy_wholesaleraccountno")
    SELECT_ENTITY_TYPE = (By.XPATH, "//div[@class='ant-space-item']/a")
    SELECT_COVERED_ENTITY_PAGE = (By.XPATH, "//span[text()='Covered Entities']")
    SELECT_PHARMACY_PAGE = (By.XPATH, "//span[text()='Pharmacies']")
    OPA_ID_NOT_FOUND_VALIDATION_MSG = (
        By.XPATH, "//span[contains(text(),'OPA ID not found. Please complete the form to add.')]")
    OPA_ID_ALREADY_EXIST_VALIDATION_MSG = (
        By.XPATH, "//span[text()='A Covered Entity with same Covered Entity Name & OPA ID already exists.']")
    SAVE_CONFIRM = (By.XPATH, "//span[text()='Save and Confirm']")
    LOCATOR1 = "//div[contains(text(),'"
    LOCATOR2 = "')]"
    ACCOUNT_NUMBER = (By.ID, "addpharmacy_wholesaleraccountno")
    MAP_PHARMACY_TO_COVERED_ENTITY = (By.XPATH, "//span[text()='Map Pharmacy to Covered Entity']")
    PHARMACY_ADDRESS = (By.ID, "addpharmacy_address")
    NPI_CODE_NOT_FOUND_VALIDATION_MSG = (
        By.XPATH, "//span[text()='NPI Code not found. Please complete the form to add.']")
    NPI_CODE_SEARCH = (By.XPATH,
                       "//label[text()='NPI Code']/parent::div/following-sibling::div/descendant::div/button/span["
                       "text()='Search']")
    ADD_COVERED_ENTITY_PAGE = (By.XPATH, "//span[text()='Add Covered Entity']/parent::div")
    SEARCH_HERE = (By.XPATH, "//input[@placeholder='Search here']")
    CE_SAVED_IN_THE_DRAFT_ALERT_MSG = (
        By.XPATH, "//span[text()='The Covered Entity and Pharmacy details saved as draft.']")
    NPI_CODE_IN_ACCORDIAN = (By.XPATH, "//span[contains(text(),'NPI Code')]/parent::div/following-sibling::div[1]")
    NABP_CODE_IN_ACCORDIAN = (By.XPATH, "//span[contains(text(),'NABP Code')]/parent::div/following-sibling::div[1]")
    PHARMACY_STORE_NUMBER_IN_ACCORDIAN = (By.XPATH, "//span[contains(text(),'Pharmacy Store Number ')]/parent::div")
    ACCOUNT_NUMBER_IN_ACCORDIAN = (By.XPATH, "//span[contains(text(),'Account Number :')]/parent::div")
    PHARMACY_TYPE_IN_ACCORDIAN = (By.XPATH, "//span[contains(text(),'Pharmacy Type :')]/parent::div")
    ADDRESS_IN_ACCORDIAN = (By.XPATH, "//span[contains(text(),'Address')]/parent::div")
    EXPANDER_IN_ACCORDIAN = (By.XPATH, "//div[@class='ant-collapse-expand-icon']")
    # CE View Page
    VIEW_SYMBOL = (By.XPATH, "//table/tbody/tr/td[1]/span")
    CE_USER_DETAILS_PAGE = (By.XPATH, "//span[text()='Covered Entity Details']")
    NAME = (By.XPATH, "//span[text()='Name']/parent::div/following-sibling::div")
    OPA_ID_IN_VIEW_PAGE = (By.XPATH, "//span[text()='OPA ID']/parent::div/following-sibling::div")
    CE_TYPE_IN_VIEW_PAGE = (By.XPATH, "//span[text()='CE Type']/parent::div/following-sibling::div")
    NO_OF_LIVE_PHARMACY_COUNT = (By.XPATH, "//span[text()='No of Live Pharmacy']/parent::div/following-sibling::div")
    NO_OF_TERM_PHARMACY = (By.XPATH, "//span[text()='No of Term Pharmacy']/parent::div/following-sibling::div")
    STATUS = (By.XPATH, "//span[text()='Status']/parent::div/following-sibling::div")
    ELIGIBILITY_RULE = (By.XPATH, "//div[text()='Eligibility Rule']")
    ADMIN_FEE = (By.XPATH, "//div[text()='Admin Fee']")
    ADD_ADMIN_FEE = (By.XPATH, "//span[text()='Add Admin Fee']")
    ADD_NEW_ADMIN_FEE = (By.XPATH, "//span[text()='Add New Admin Fee']")
    NEW_ADMIN_FEE_POP_UP = (By.XPATH, "//span[text()='Are you sure you want to add new Admin fee?']")
    ADMIN_FEE_ALERT_NOTE = (By.XPATH, "//span[text()='Note : Previous admin fee will be moved to history.']")
    ADMIN_FEE_SAVE = (By.XPATH,
                      "//span[contains(text(),'Admin Fee')]/parent::div/parent::div/parent::div/following-sibling"
                      "::div/descendant::button/span[text()='Save']")
    NEW_ADMIN_FEE_SAVE = (By.XPATH,
                          "//span[contains(text(),'New')]/parent::div/parent::div/parent::div/following-sibling::div/descendant::button/span[text()='Save']")
    RULE1_SAVE_BUTTON = (By.XPATH,
                         "//span[contains(text(),'Rule 1')]/parent::div/parent::div/parent::div/following-sibling::div/descendant::button/span[text()='Save']")
    RULE2_SAVE_BUTTON = (By.XPATH,
                         "//span[contains(text(),'Patient Eligibility Term Date')]/parent::div/parent::div/parent::div/following-sibling::div/descendant::button/span[text()='Save']")
    UPDATE_LIVE_TERM_DATE = (By.XPATH, "//span[text()='Update Live Date & Term Date']")
    DATE_SAVED_SUCCESS_MSG = (By.XPATH, "//span[text()='Data Saved Successfully']")
    LIVE_TERM_DATE_SUCCESS_MSG = (By.XPATH, "//div[text()='Live date and Term date updated successfully.']")
    CLOSE_ICON = (By.XPATH, "//span[@class='ant-modal-close-x']")
    PATIENT_ELIGIBILITY_TERM_DATE = (By.XPATH, "//input[@role='spinbutton']")
    PATIENT_ELIGIBILITY_TERM_DATE_SUC_MSG = (
        By.XPATH, "//div[text()='Patient Eligibility Term Date saved successfully']")
    RULE_1_EDIT_BUTTON = (
        By.XPATH, "//span[contains(text(),'Rule 1')]/parent::div/following-sibling::div/descendant::span")
    RULE_2_EDIT_OPTION = (
        By.XPATH, "//span[contains(text(),'Rule 2')]/parent::div/following-sibling::div/descendant::span")
    ADMIN_FEE_EDIT_OPTION = (By.XPATH, "//span[text()='Admin Fee']/parent::div/following-sibling::div/descendant::span")
    NEW_ADMIN_FEE_EDIT_OPTION = (
        By.XPATH, "//span[text()='New Admin Fee']/parent::div/following-sibling::div/descendant"
                  "::span")
    RULE_2_SAVE_BUTTON = (
        By.XPATH, "//span[contains(text(),'Rule 2')]/parent::div/following-sibling::div/descendant::span")
    UPDATE_ADMIN_FEE = (By.XPATH, "//span[text()='Update Admin Fee']")
    UPDATE_ADMIN_FEE_POPUP = (By.XPATH, "//div[contains(text(),'Are you sure you want to update the Admin fee?')]")
    UPDATE_PATIENT_ELIGIBILITY_TERM_DATE = (By.XPATH, "//span[text()='Update Patient Eligibility Term Date']")
    PATIENT_ELIGIBILITY_ALERT_MSG = (By.XPATH, "//div[text()='Are you sure you want to update the Patient Eligibility "
                                               "Term date?']")
    UPDATE_TERM_DATE = (By.XPATH, "//span[text()='Update Term Date']")
    UPDATE_TERM_DATE_ALERT_MSG = (By.XPATH, "//div[text()='Are you sure you want to update the term date?']")
    UPDATED_PATIENT_TERM_DATE_SUC_MSG = (By.XPATH, "//div[text()='Patient Eligibility Term Date saved successfully']")
    PERCENTAGE_OF_NET = (By.NAME, "flatfee")
    SELECT_BILLING_MODEL = (
        By.XPATH, "//input[@role='combobox']/parent::span/following-sibling::span[text()='Select Billing Model']")
    # Preview Page
    OPA_ID_IN_PREVIEW_PAGE = (By.XPATH, "//span[text()='OPA ID']/parent::div/following-sibling::div[2]")
    PHARMACY_NAME_IN_PREVIEW_PAGE = (By.XPATH, "//span[text()='Pharmacy Name']/parent::div/following-sibling::div[2]")
    CE_TYPE_IN_PREVIEW_PAGE = (By.XPATH, "//span[text()='Covered Entity Type']/parent::div/following-sibling::div[2]")
    CE_NAME_IN_PREVIEW_PAGE = (By.XPATH, "//span[text()='Covered Entity Name']/parent::div/following-sibling::div[2]")
    ADDRESS_IN_PREVIEW_PAGE = (By.XPATH, "//span[text()='Address']/parent::div/following-sibling::div[2]")
    NPI_CODE_IN_PREVIEW_PAGE = (By.XPATH, "//span[text()='NPI Code']/parent::div/following-sibling::div[2]")
    NABP_CODE_IN_PREVIEW_PAGE = (By.XPATH, "//span[text()='NABP Code']/parent::div/following-sibling::div[2]")
    PHARMACY_TYPE_IN_PREVIEW_PAGE = (By.XPATH, "//span[text()='Pharmacy Type']/parent::div/following-sibling::div[2]")
    PHARMACY_STORE_NUMBER_IN_PREVIEW_PAGE = (
        By.XPATH, "//span[text()='Pharmacy Store Number']/parent::div/following-sibling::div[2]")
    WHOLESALER_IN_PREVIEW_PAGE = (By.XPATH, "//span[text()='Wholesaler']/parent::div/following-sibling::div[2]")
    ACCOUNT_NUMBER_IN_PREVIEW_PAGE = (By.XPATH, "//span[text()='Account Number']/parent::div/following-sibling::div[2]")
    CONFIRM_BUTTON = (By.XPATH, "//span[text()='Confirm']")
    NEW_CE_ADDED_VALIDATION_MSG = (By.XPATH, "//span[text()='New Covered Entity is successfully added!']")
    GO_TO_CE_LIST = (By.XPATH, "//span[text()='Go to Covered Entity List']")
    # Pharmacy Page
    ADD_PHARMACY_BUTTON = (By.XPATH, "//span[contains(text(), 'Add Pharmacy')]")

    def get_admin_fee_suc_msg(self, text):
        return self.driver.find_element(By.XPATH,
                                        "//span[contains(text(),'Admin fee for " + text + " set Successfully.')]")

    def verify_view_button_in_grid(self, opaId):
        self.verify_element_present(self.CONFIGURATION_MANAGEMENT, 30)
        self.click_element(self.CONFIGURATION_MANAGEMENT)
        self.verify_element_present(self.SEARCH_HERE, 10)
        self.send_Keys(self.SEARCH_HERE, opaId)
        self.verify_element_present(self.VIEW_SYMBOL, 20)
        assert self.element_visible(CoveredEntity.VIEW_SYMBOL) == True
        self.click_element(self.VIEW_SYMBOL)

    def navigate_to_pharmacies(self):
        self.verify_element_present(self.CONFIGURATION_MANAGEMENT, 30)
        self.click_element(self.CONFIGURATION_MANAGEMENT)
        self.move_to_Element(self.SELECT_ENTITY_TYPE)
        self.verify_element_present(self.SELECT_PHARMACY_PAGE, 10)
        self.click_element(self.SELECT_PHARMACY_PAGE)
        self.verify_element_present(self.ADD_PHARMACY_BUTTON, 30)
        assert self.element_visible(self.ADD_PHARMACY_BUTTON) == True

    def verify_existing_opaid(self, opaID):
        self.verify_element_present(self.CONFIGURATION_MANAGEMENT, 20)
        self.click_element(self.CONFIGURATION_MANAGEMENT)
        self.click_element(self.ADD_CE_BUTTON)
        self.verify_element_present(self.OPA_ID_SEARCH, 20)
        self.send_Keys(self.OPA_ID, opaID)
        self.click_element(self.OPA_ID_SEARCH)
        self.click_element(self.CONTINUE_BUTTON)

    def adding_admin_fee(self, date, selectBillingModelType, number, ceName):
        action = ActionChains(self.driver)
        # self.select_date("Start Date", date)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//span[contains(text(),'Start "
                                          "Date')]/parent::div/following-sibling::div/descendant::input").send_keys(date)
        action.send_keys(Keys.ENTER).perform()
        time.sleep(2)
        self.move_to_Element(self.SELECT_BILLING_MODEL)
        action.click().perform()
        button = self.driver.find_element(By.XPATH, "//div[contains(text(),'" + selectBillingModelType + "')]")
        button.click()
        self.send_Keys(self.PERCENTAGE_OF_NET, number)

    def accordian(self, npiCode, nabpCode, pharmacyStoreNum, pharmacyType, pharmacyAdd, pharmacy_acc_num):
        self.verify_element_present(self.MAP_PHARMACY_TO_COVERED_ENTITY, 10)
        self.verify_element_present(self.NPI_CODE_IN_ACCORDIAN, 10)
        assert self.get_text(self.NPI_CODE_IN_ACCORDIAN) in npiCode
        assert self.get_text(self.NABP_CODE_IN_ACCORDIAN) in nabpCode
        self.verify_element_present(self.EXPANDER_IN_ACCORDIAN, 10)
        self.click_element(self.EXPANDER_IN_ACCORDIAN)
        self.verify_element_present(self.PHARMACY_STORE_NUMBER_IN_ACCORDIAN, 10)
        pharmacy_store_number = self.get_text(self.PHARMACY_STORE_NUMBER_IN_ACCORDIAN)
        psn = pharmacy_store_number.split(":")[1]
        assert psn.split(" ")[1] in pharmacyStoreNum
        pharmacy_type = self.get_text(self.PHARMACY_TYPE_IN_ACCORDIAN)
        pt = pharmacy_type.split(":")[1]
        assert pt.split(" ")[1] in pharmacyType
        pharmacy_address = self.get_text(self.ADDRESS_IN_ACCORDIAN)
        pa = pharmacy_address.split(":")[1]
        assert pa.split(" ")[1] in pharmacyAdd
        pharmacy_account_number = self.get_text(self.ACCOUNT_NUMBER_IN_ACCORDIAN)
        pan = pharmacy_account_number.split(":")[1]
        assert pan.split(" ")[1] in pharmacy_acc_num

    def add_admin_fee(self, date, selectBillingModelType, number, ceName, adminFee):
        self.verify_element_present(self.ADMIN_FEE, 20)
        self.click_element(self.ADMIN_FEE)
        if adminFee == "":
            self.adding_admin_fee(date, selectBillingModelType, number, ceName)
            self.click_element(self.ADMIN_FEE_SAVE)
            self.get_admin_fee_suc_msg(ceName).is_displayed()
            time.sleep(2)
            self.click_element(self.CLOSE_ICON)
            self.verify_element_present(self.ADMIN_FEE, 10)
        if adminFee == "add":
            self.click_element(self.ADD_ADMIN_FEE)
            self.adding_admin_fee(date, selectBillingModelType, number, ceName)
            self.click_element(self.NEW_ADMIN_FEE_SAVE)
            self.verify_element_present(self.ADD_NEW_ADMIN_FEE, 15)
            assert "Add New Admin Fee" in self.get_text(self.ADD_NEW_ADMIN_FEE)
            assert self.element_visible(self.NEW_ADMIN_FEE_POP_UP) == True
            assert self.element_visible(self.ADMIN_FEE_ALERT_NOTE) == True
            self.click_element(self.CONFIRM_BUTTON)
            self.get_admin_fee_suc_msg(ceName).is_displayed()
            time.sleep(2)
            self.click_element(self.CLOSE_ICON)
            time.sleep(2)
            self.verify_element_present(self.ADMIN_FEE, 10)

    def search_new_covered_entity(self, opaID, coveredEntity, liveDate, termDate):
        log = self.get_logger()
        self.verify_element_present(self.CONFIGURATION_MANAGEMENT, 10)
        self.click_element(self.CONFIGURATION_MANAGEMENT)
        self.send_Keys(self.SEARCH_HERE, opaID)
        self.search_user(LoginPage.TOTAL_ROWS, 1, 1, LoginPage.SINGLE_ROW, LoginPage.SINGLE_COLUMN, opaID,
                         coveredEntity,
                         liveDate, 'Pending', "CoveredEntity", termDate)
        log.info(opaID)

    def verify_add_ce_page(self):
        self.verify_element_present(self.CONFIGURATION_MANAGEMENT, 30)
        self.click_element(self.CONFIGURATION_MANAGEMENT)
        self.verify_element_present(self.ADD_CE_BUTTON, 30)
        self.click_element(self.ADD_CE_BUTTON)
        self.verify_element_present(self.ADD_COVERED_ENTITY_PAGE, 20)
        opaid_search = self.element_visible(self.OPA_ID_SEARCH)
        assert opaid_search == True
        ce_name_search = self.element_visible(self.CE_NAME_SEARCH)
        assert ce_name_search == True

    def add_pharmacy(self, npiCode, phName, nabpCode, pharmacyType, pharmacyStoreNumber, address, wholesalerType,
                     wholesalerAccountNum):
        self.verify_element_present(self.MAP_PHARMACY_TO_COVERED_ENTITY, 30)
        self.element_visible(self.NPI_CODE_SEARCH)
        self.verify_element_present(self.NPI_CODE, 20)
        self.element_visible(self.PHARMACY_NAME)
        self.send_Keys(self.NPI_CODE, npiCode)
        self.send_Keys(self.PHARMACY_NAME, phName)
        self.send_Keys(self.NABP_CODE, nabpCode)
        self.click_dropdown(self.PHARMACY_TYPE, CoveredEntity.LOCATOR1, CoveredEntity.LOCATOR2,
                            pharmacyType)
        self.send_Keys(self.PHARMACY_STORE_NUMBER, pharmacyStoreNumber)
        self.send_Keys(self.PHARMACY_ADDRESS, address)
        self.click_dropdown(self.SELECT_PHARMACY_WHOLESALER, CoveredEntity.LOCATOR1,
                            CoveredEntity.LOCATOR2,
                            wholesalerType)
        self.send_Keys(self.WHOLESALER_ACCOUNT_NUMBER, wholesalerAccountNum)

    def covered_entity_details_preview(self, opaId, ceType, ceName):
        self.verify_element_present(self.OPA_ID_IN_PREVIEW_PAGE, 20)
        opa_id = self.get_text(self.OPA_ID_IN_PREVIEW_PAGE)
        assert opa_id in opaId
        ce_type = self.get_text(self.CE_TYPE_IN_PREVIEW_PAGE)
        assert ce_type in ceType
        ce_name = self.get_text(self.CE_NAME_IN_PREVIEW_PAGE)
        assert ce_name in ceName

    def pharmacy_details_preview(self, phName, npiCode, nabpCode, pharmacyType, pharmacyStoreNum, Wholesaler,
                                 accountNumber):
        self.verify_element_present(self.PHARMACY_NAME_IN_PREVIEW_PAGE, 20)
        pharmacy_name = self.get_text(self.PHARMACY_NAME_IN_PREVIEW_PAGE)
        assert pharmacy_name == phName
        npi_code = self.get_text(self.NPI_CODE_IN_PREVIEW_PAGE)
        assert npi_code == npiCode
        nabp_code = self.get_text(self.NABP_CODE_IN_PREVIEW_PAGE)
        assert nabp_code == nabpCode
        pharmacy_type = self.get_text(self.PHARMACY_TYPE_IN_PREVIEW_PAGE)
        assert pharmacy_type == pharmacyType
        pharmacy_store_number = self.get_text(self.PHARMACY_STORE_NUMBER_IN_PREVIEW_PAGE)
        assert pharmacy_store_number == pharmacyStoreNum
        wholesaler = self.get_text(self.WHOLESALER_IN_PREVIEW_PAGE)
        assert wholesaler == Wholesaler
        account_number = self.get_text(self.ACCOUNT_NUMBER_IN_PREVIEW_PAGE)
        assert account_number == accountNumber

    def cf_table_page_nation_dropdowns(self):
        self.verify_element_present(self.CONFIGURATION_MANAGEMENT, 30)
        self.click_element(self.CONFIGURATION_MANAGEMENT)
        self.verify_table_page_nations_dropdowns()
        time.sleep(5)

    def cf_table_page_nations(self):
        self.refresh()
        time.sleep(2)
        self.verify_element_present(self.CONFIGURATION_MANAGEMENT, 20)
        time.sleep(2)
        self.click_element(self.CONFIGURATION_MANAGEMENT)
        self.verify_page_nations_in_table()

    def ce_view_user(self, name, opaId, noOfLivePharmacy, noOfTermPharmacy, Status):
        log = self.get_logger()
        self.verify_element_present(self.CONFIGURATION_MANAGEMENT, 20)
        self.click_element(self.CONFIGURATION_MANAGEMENT)
        time.sleep(1)
        self.verify_element_present(self.SEARCH_HERE, 20)
        self.send_Keys(self.SEARCH_HERE, opaId)
        self.click_element(self.VIEW_SYMBOL)
        self.verify_element_present(self.CE_USER_DETAILS_PAGE, 20)
        ph_name = self.get_text(self.NAME)
        log.info(ph_name)
        assert ph_name == name
        opa_id = self.get_text(self.OPA_ID_IN_VIEW_PAGE)
        log.info(opa_id)
        assert opa_id == opaId
        ce_type = self.get_text(self.CE_TYPE_IN_VIEW_PAGE)
        log.info(ce_type)
        # assert ce_type == ceType
        no_of_live_pharmacy = self.get_text(self.NO_OF_LIVE_PHARMACY_COUNT)
        log.info(no_of_live_pharmacy)
        assert no_of_live_pharmacy == noOfLivePharmacy
        no_of_term_pharmacy = self.get_text(self.NO_OF_TERM_PHARMACY)
        log.info(no_of_term_pharmacy)
        assert no_of_term_pharmacy == noOfTermPharmacy
        status = self.get_text(self.STATUS)
        log.info(status)
        assert status == Status

    def eligibility_rule(self, liveDate, termDate, updateDate, liveTermDate):
        self.select_date("Live Date", liveDate)
        self.select_date("Term Date", termDate)
        self.click_element(self.RULE1_SAVE_BUTTON)
        time.sleep(1)
        self.verify_element_present(self.DATE_SAVED_SUCCESS_MSG, 10)
        live_term_date_msg = self.get_text(self.LIVE_TERM_DATE_SUCCESS_MSG)
        assert live_term_date_msg == liveTermDate
        self.verify_element_present(self.CLOSE_ICON, 10)
        self.click_element(self.CLOSE_ICON)

    def update_term_date(self, updateDate):
        self.verify_element_present(self.ELIGIBILITY_RULE, 20)
        self.verify_element_present(self.RULE_1_EDIT_BUTTON, 10)
        self.click_element(self.RULE_1_EDIT_BUTTON)
        self.select_date("Term Date", updateDate)
        self.click_element(self.RULE1_SAVE_BUTTON)
        time.sleep(1)
        self.verify_element_present(self.UPDATE_TERM_DATE, 20)
        assert self.element_visible(self.UPDATE_TERM_DATE) == True
        assert "Are you sure you want to update the term date?" in self.get_text(self.UPDATE_TERM_DATE_ALERT_MSG)
        self.click_element(self.CONFIRM_BUTTON)
        time.sleep(1)
        self.verify_element_present(self.DATE_SAVED_SUCCESS_MSG, 20)
        assert self.element_visible(self.DATE_SAVED_SUCCESS_MSG) == True
        assert "Live date and Term date updated successfully." in self.get_text(self.LIVE_TERM_DATE_SUCCESS_MSG)
        self.verify_element_present(self.CLOSE_ICON, 20)
        self.click_element(self.CLOSE_ICON)

    def patient_eligibility_term_date(self, eligibilityTermDate, eligibilityTermDateSucMsg, patientEligibility):
        self.verify_element_present(self.PATIENT_ELIGIBILITY_TERM_DATE, 20)
        if patientEligibility == "AddPatientEligibility":
            self.send_Keys(self.PATIENT_ELIGIBILITY_TERM_DATE, eligibilityTermDate)
            self.click_element(self.RULE2_SAVE_BUTTON)
            time.sleep(1)
            self.verify_element_present(self.DATE_SAVED_SUCCESS_MSG, 30)
            assert self.element_visible(self.DATE_SAVED_SUCCESS_MSG) == True
            assert eligibilityTermDateSucMsg in self.get_text(self.PATIENT_ELIGIBILITY_TERM_DATE_SUC_MSG)
            self.click_element(self.CLOSE_ICON)
        if patientEligibility == "UpdatePatientEligibility":
            self.click_element(self.RULE_2_EDIT_OPTION)
            self.send_Keys(self.PATIENT_ELIGIBILITY_TERM_DATE, eligibilityTermDate)
            self.click_element(self.RULE2_SAVE_BUTTON)
            time.sleep(1)
            self.verify_element_present(self.UPDATE_PATIENT_ELIGIBILITY_TERM_DATE, 10)
            assert self.element_visible(self.UPDATE_PATIENT_ELIGIBILITY_TERM_DATE) == True
            assert "Are you sure you want to update the Patient Eligibility Term date?" in self.get_text(
                self.PATIENT_ELIGIBILITY_ALERT_MSG)
            self.click_element(self.CONFIRM_BUTTON)
            self.verify_element_present(self.DATE_SAVED_SUCCESS_MSG, 30)
            assert eligibilityTermDateSucMsg in self.get_text(self.PATIENT_ELIGIBILITY_TERM_DATE_SUC_MSG)
            self.click_element(self.CLOSE_ICON)

    def add_new_covered_entity(self, opaId, ceName, ceType, npiCode, phName, nabpCode, pharmacyType,
                               pharmacyStoreNumber, address, wholesalerType, wholesalerAccountNum):
        log = self.get_logger()
        action = ActionChains(self.driver)
        self.verify_element_present(self.CONFIGURATION_MANAGEMENT, 30)
        self.click_element(self.CONFIGURATION_MANAGEMENT)
        self.verify_element_present(self.ADD_CE_BUTTON, 20)
        self.click_element(self.ADD_CE_BUTTON)
        self.verify_element_present(self.OPA_ID, 30)
        self.element_visible(self.CE_NAME)
        self.send_Keys(self.OPA_ID, opaId)
        log.info(opaId)
        self.click_element(self.OPA_ID_SEARCH)
        self.element_visible(self.OPA_ID_NOT_FOUND_VALIDATION_MSG)
        self.send_Keys(self.CE_NAME, ceName)
        self.move_to_Element(self.CE_TYPE)
        action.click().perform()
        button = self.driver.find_element(By.XPATH, "//div[contains(text(),'" + ceType + "')]")
        button.click()
        self.click_element(self.ADD_CONTINUE)
        self.add_pharmacy(npiCode, phName, nabpCode, pharmacyType, pharmacyStoreNumber, address, wholesalerType,
                          wholesalerAccountNum)
        self.click_element(self.SAVE_CONFIRM)
        self.covered_entity_details_preview(opaId, ceType, ceName)
        self.pharmacy_details_preview(phName, npiCode, nabpCode, pharmacyType, pharmacyStoreNumber, wholesalerType,
                                      wholesalerAccountNum)
        self.click_element(self.SAVE_BUTTON)
        self.verify_element_present(self.CE_SAVED_IN_THE_DRAFT_ALERT_MSG, 10)
        ce_saved_alert = self.get_text(self.CE_SAVED_IN_THE_DRAFT_ALERT_MSG)
        assert ce_saved_alert == "The Covered Entity and Pharmacy details saved as draft."
        self.click_element(self.CONFIRM_BUTTON)
        self.verify_element_present(self.NEW_CE_ADDED_VALIDATION_MSG, 30)
        new_ce_added = self.get_text(self.NEW_CE_ADDED_VALIDATION_MSG)
        assert new_ce_added == "New Covered Entity is successfully added!"
        self.click_element(self.GO_TO_CE_LIST)
        self.verify_element_present(self.ADD_CE_BUTTON, 20)
