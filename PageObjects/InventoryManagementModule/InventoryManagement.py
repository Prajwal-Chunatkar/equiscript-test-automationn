from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass

class Inventory(object):
    INVENTORY_MGMNT = "//span[text()='Inventory Management']"
    ADD_SEARCH = (By.XPATH, "//span[text()=' Add Search Criteria']")
    FIELD_NAME = (By.XPATH,"//span[text()='Field Name']")
    OPERATOR = (By.XPATH,"//span[text()='Operator']")
    VALUE = (By.XPATH,"//span[text()='Operator']")
    ENTITY = (By.XPATH, "//span[text()='Select Field Name']//preceding-sibling::span")
    Loc1 = "//div[@title='"
    Loc2 = "']"
    SEARCH_CE_NAME = (By.XPATH, "//span[text() ='Search Covered Entity']/../descendant::input")
    APPLY_FILTER = (By.XPATH, "//span[text()='Apply Filter']/..")
    PHARMACY = (By.XPATH, "//span[text()='Pharmacy']")
    PHARMACY_NPI = (By.XPATH, "//span[text()='Pharmacy NPI']")
    CHAIN_PHARMACY = (By.XPATH, "//span[text()='Chain Pharmacy']")
    NDC = (By.XPATH, "//span[text()='NDC']")
    DRUG_NAME = (By.XPATH, "//span[text()='Drug Name']")
    DRUG_TYPE = (By.XPATH, "//span[text()='Drug type']")
    DRUG_CLASS = (By.XPATH, "//span[text()='Drug Class']")
    MFG_NAME = (By.XPATH, "//span[text()='MFG Name']")
    DISPENSED_LINK = (By.XPATH,"(//table//tbody//td[count(//span[text()='Dispensed Qty']//ancestor::th/preceding-sibling::th)+1]//a)[1]")
    DISPQTY_INFO = (By.XPATH,"//span[contains(text(),'Dispensed Qty -')]")
    CLAIMS_TYPE = (By.XPATH, "//span[text()='Claim Type']")
    CLAIMS_ID = (By.XPATH, "//span[text()='Claim ID']")
    RX_NUM = (By.XPATH, "//span[text()='RX number']")
    DISP_QTY_ELES = "//span[text()='Dispensed Qty']"
    REFILL_CODE = (By.XPATH, "//span[text()='Refill Code']")
    PHARMACY_NAME = (By.XPATH, "//span[@title='Pharmacy Name']")
    RX_NUM_LINK = (By.XPATH,"(//table//tbody//td[count(//span[text()='RX number']//ancestor::th/preceding-sibling::th)+1]//a)[1]")
    BREADCRUMB = (By.XPATH,"//span[contains(@class,'breadcrumb')]//span")
    ##RX details Xpath
    RX_WRITTEN = (By.XPATH, "//span[text()='RX Written']")
    RX_FILLED = (By.XPATH, "//span[text()='RX Filled']")
    CLAIM_PROCESSED = (By.XPATH, "//span[text()='Claim Processed']")
    REVERSED = (By.XPATH, "//span[text()='Reversed']")
    CLAIM_HISTORY = (By.XPATH, "//span[text()='Claim History']")
    VISIT_HISTORY = (By.XPATH, "//span[text()='Visit History']")
    DRUG_COST = (By.XPATH, "//span[text()='Drug Costs']")
    BASIC_DETAILS = (By.XPATH, "//span[text()='Basic Details']")
    BACK_ARROW = (By.XPATH, "//span[@role='img' and @aria-label='arrow-left']")
    PO_LINK = (By.XPATH,"(//table//tbody//td[count(//span[text()='PO #']//ancestor::th/preceding-sibling::th)+1]//a)[1]")
    ##Order Details Screen Xpath
    ORDER_AKN = (By.XPATH, "//span[text()='Order Acknowledgement']")
    ORDER_INVOICE = (By.XPATH, "//span[text()='Order Invoiced']")
    ORDER_CREATION_DATE = (By.XPATH, "//span[text()='Order Creation Date']")
    PO_STATUS = (By.XPATH, "//span[text()='PO Status']")
    PO_NUMBER = (By.XPATH, "//span[text()='PO Number']")

class InventoryManagement(BaseClass):

    def __init__(self,driver):
        self.driver = driver

    def validate_inventory_management_page(self):
            elements = self.get_webelements(Inventory.INVENTORY_MGMNT)
            checklist = ['inventory' in self.driver.current_url, len(elements) > 1,
                         self.element_visible(Inventory.ADD_SEARCH)]
            assert not (False in checklist), " element not present on Claim Management screen"

    def add_search_crieteria(self):
        self.click_element(Inventory.ADD_SEARCH)
        checklist = [self.element_visible(Inventory.FIELD_NAME), self.element_visible(Inventory.OPERATOR),
                     self.element_visible(Inventory.VALUE)]
        assert not (False in checklist), " element not present on Claim Management screen"

    def select_data_for_inventory_and_validate(self,entityname):
        self.wait_till_dropdown_clickable_and_select(Inventory.ENTITY,Inventory.Loc1,Inventory.Loc2,"Covered Entity")
        self.search_dropdown_and_select(Inventory.SEARCH_CE_NAME,Inventory.Loc1,Inventory.Loc2,entityname)
        self.click_element(Inventory.APPLY_FILTER)
        checklist = [self.element_visible(Inventory.PHARMACY),self.element_visible(Inventory.PHARMACY_NPI),
                     self.element_visible(Inventory.CHAIN_PHARMACY),self.element_visible(Inventory.NDC),
                     self.element_visible(Inventory.DRUG_NAME),self.element_visible(Inventory.DRUG_TYPE),
                     self.element_visible(Inventory.DRUG_CLASS),self.element_visible(Inventory.MFG_NAME)]
        assert not (False in checklist), " element not present on Claim Management screen"

    def validate_navigation_to_dispense_qty_info(self):
        self.click_element(Inventory.DISPENSED_LINK)
        eles = self.get_webelements(Inventory.DISP_QTY_ELES)
        checklist = [self.element_visible(Inventory.DISPQTY_INFO),len(eles)>1,
                     self.element_visible(Inventory.CLAIMS_TYPE),self.element_visible(Inventory.CLAIMS_ID),
                     self.element_visible(Inventory.RX_NUM)]
        assert not (False in checklist), " element not present on Dispensed Qty Claim Info screen"

    def validate_navigation_to_rx_details_screen(self):
        self.click_element(Inventory.RX_NUM_LINK)
        RX_Details_Present = self.get_text(Inventory.BREADCRUMB).lower() == "RX Details".lower()
        checklist = [RX_Details_Present,self.element_visible(Inventory.RX_WRITTEN),
                     self.element_visible(Inventory.RX_FILLED), self.element_visible(Inventory.CLAIM_PROCESSED),
                     self.element_visible(Inventory.CLAIM_HISTORY),self.element_visible(Inventory.VISIT_HISTORY),
                     self.element_visible(Inventory.DRUG_COST),self.element_visible(Inventory.BASIC_DETAILS),
                     self.element_visible(Inventory.BACK_ARROW)]
        assert not (False in checklist), " element not present on Dispensed Qty Claim Info screen"

    def validate_navigation_to_PO_details_screen(self):
        self.click_element(Inventory.PO_LINK)
        Order_Details_Present = self.get_text(Inventory.BREADCRUMB).lower() == "Order Details".lower()
        checklist = [Order_Details_Present, self.element_visible(Inventory.PO_NUMBER),
                     self.element_visible(Inventory.PO_STATUS), self.element_visible(Inventory.ORDER_CREATION_DATE),
                     self.element_visible(Inventory.ORDER_INVOICE), self.element_visible(Inventory.ORDER_AKN),
                     self.element_visible(Inventory.BACK_ARROW)]
        assert not (False in checklist), " element not present on Dispensed Qty Claim Info screen"





