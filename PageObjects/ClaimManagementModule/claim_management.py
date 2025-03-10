from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass


class Claims(object):
    # ADD_SEARCH = (By.XPATH,"//span[text()=' Add Search Criteria']")
    # CLAIMS_MANAGEMENT = "//span[text()='Claims Management']"
    FIELD_NAME = (By.XPATH,"//span[text()='Field Name']")
    OPERATOR = (By.XPATH,"//span[text()='Operator']")
    VALUE = (By.XPATH,"//span[text()='Value']")
    ENTITY = (By.XPATH,"//span[text()='Select Field Name']//preceding-sibling::span")
    SEARCH_CE = (By.XPATH,"//span[text()='Search Covered Entity']")

    SEARCH_CE_NAME = (By.XPATH,"//span[text() ='Search Covered Entity']/../descendant::input")
    SELECT_CE = (By.XPATH,"//div[text()='AltaMed Health Services Corporation']")
    SELECT_OPERATOR = (By.XPATH,"//input[contains(@id,'operator')]")
    EQUALS_TO = (By.XPATH,"//span[@title='= Equals to']")
    APPLY_FILTER = (By.XPATH,"//span[text()='Apply Filter']/..")
    CLAIMS_LIST = (By.XPATH,"//span[text()='Claims List']")
    RX_NUM = (By.XPATH,"//span[text()='Rx Number']")
    REFILL_CODE = (By.XPATH,"//span[text()='Refill Code']")
    CLAIM_DATE = (By.XPATH,"//span[text()='Claim Process Date']")
    CLAIM_STATUS= (By.XPATH,"//span[text()='Claim Status']")
    PHARMACY_NPI= (By.XPATH,"//span[@title='Pharmacy NPI']")
    PHARMACY_NAME= (By.XPATH,"//span[@title='Pharmacy Name']")
    Loc1 = "//div[@title='"
    Loc2 = "']"
    CAPTURED = "//div[contains(@class,'ant-space-align-baseline')]//child::button//span"
    CLAIM_SAVING_OP = (By.XPATH,"//div[@class='ant-space-item']//child::span[text()='Opportunity Claims Savings']")
    TABLE_ROWS = "//table//tbody//tr"
    CLAIM_CAPTURED_STATUS = "//table/tbody/tr/td[count(//table//thead/tr/th/div/span[text()='Claim Status']/../../preceding-sibling::th)+1]"
    CLAIM_COUNT = "//div[contains(@class,'ant-space-align-baseline')]//child::button//span"
    # LOCATOR1 = "//div[contains(text(),'"
    # LOCATOR2 = "')]"


class ClaimManagement(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def verify_claims_management_page(self):
        elements = self.get_webelements_bytext('Claims Management')
        checklist = ['claims' in self.driver.current_url ,len(elements ) >1,
                     self.verify_element_present_bytext(' Add Search Criteria',30)]
        assert not (False in checklist), " element not present on Claim Management screen"

    def add_search_crieteria(self):
        self.click_element_bytext(' Add Search Criteria')
        checklist = [self.element_visible(Claims.FIELD_NAME),self.element_visible(Claims.OPERATOR),
                     self.element_visible(Claims.VALUE)]
        assert not (False in checklist), " element not present on Claim Management screen"


    def select_data_for_claim_and_validate(self,entityname):
        self.wait_till_dropdown_clickable_and_select(Claims.ENTITY,Claims.Loc1,Claims.Loc2,"Covered Entity")
        self.search_dropdown_and_select(Claims.SEARCH_CE_NAME,Claims.Loc1,Claims.Loc2,entityname)
        self.click_element(Claims.APPLY_FILTER)
        checklist = [self.element_visible(Claims.CLAIMS_LIST),self.element_visible(Claims.RX_NUM),
                     self.element_visible(Claims.CLAIM_DATE),self.element_visible(Claims.CLAIM_STATUS),
                     self.element_visible(Claims.REFILL_CODE)]
        assert not (False in checklist), " element not present on Claim Management screen"


    def verify_capture_non_captured(self):
        checklist=[]
        eles = self.get_webelements(Claims.CAPTURED)
        eles.pop(0)
        for ele in eles:
            if 'Capture'.lower() in ele.text.lower():
                checklist.append(True)
            else:
                checklist.append(False)
        assert not (False in checklist), " element not present on Claim Management screen"
        ##Validate total count equal to capt and non-captured count
        elements = self.get_webelements(Claims.CLAIM_COUNT)
        count = []
        for element in elements:
            count.append(element.text.split("(")[1][0:].replace(")","").replace(',',""))
        assert int(count[0])==int(count[1])+int(count[2]),"claim count mismatch found"



    def verify_claim_saving_opportunity(self):
        self.click_element(Claims.CLAIM_SAVING_OP)
        rows = self.get_webelements(Claims.TABLE_ROWS)
        assert len(rows)>1==True,"table data for opportunity for claim saving is empty"

    def verify_claim_status(self):
        checklist = []
        eles = self.get_webelements(Claims.CLAIM_CAPTURED_STATUS)
        for i in range (1,len(eles)):
            if eles[i].text.lower()=="Non Captured".lower():
                checklist.append(True)
            else:
                assert False , f"{eles[i].text.lower()} status does not match "
        assert not (False in checklist), " element not present on Claim Management screen"




