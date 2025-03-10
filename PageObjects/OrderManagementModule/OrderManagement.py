from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass


class Order_Endpoint(object):
    ORDER_MGMNT = "//span[text()='Order Management']"
    SEARCH_FILTER = (By.XPATH, "//span[contains(text(),'Search Filters')]")
    ADD_SEARCH = (By.XPATH, "//span[text()=' Add Search Criteria']")
    ENTITY = (By.XPATH, "//span[text()='Select Field Name']//preceding-sibling::span")
    SEARCH_CE = (By.XPATH, "//span[text()='Search Covered Entity']")

    SEARCH_CE_NAME = (By.XPATH, "//span[text() ='Search Covered Entity']/../descendant::input")
    EQUALS_TO = (By.XPATH, "//span[@title='= Equals to']")
    APPLY_FILTER = (By.XPATH, "//span[text()='Apply Filter']/..")
    PHARMACY_NPI = (By.XPATH, "//span[text()='Pharmacy NPI']")
    WHOLESALER = (By.XPATH, "//span[text()='Wholesaler']")
    WHOLESALER_ACC = (By.XPATH, "//span[text()='Wholesaler Account']")
    RX_NUM = (By.XPATH, "//span[text()='Rx Number']")
    REFILL_CODE = (By.XPATH, "//span[text()='Refill Code']")
    CLAIM_DATE = (By.XPATH, "//span[text()='Claim Process Date']")
    CLAIM_STATUS = (By.XPATH, "//span[text()='Claim Status']")
    PHARMACY_NAME = (By.XPATH, "//span[@title='Pharmacy Name']")
    Loc1 = "//div[@title='"
    Loc2 = "']"
    CAPTURED = "//div[contains(@class,'ant-space-align-baseline')]//child::button//span"
    CLAIM_SAVING_OP = (By.XPATH, "//div[@class='ant-space-item']//child::span[text()='Opportunity Claims Savings']")
    TABLE_ROWS = "//table//tbody//tr"
    PO_NUMBER_LINK = (By.XPATH,
                      "(//table/tbody/tr/td[count(//table//thead/tr/th/div/span[text()='PO Number ']/../../preceding-sibling::th)+1]//a)[1]")
    CLAIM_COUNT = "//div[contains(@class,'ant-space-align-baseline')]//child::button//span"
    ORDER_AKN = (By.XPATH, "//span[text()='Order Acknowledgement']")
    ORDER_INVOICE = (By.XPATH, "//span[text()='Order Invoiced']")
    ORDER_CREATION_DATE = (By.XPATH, "//span[text()='Order Creation Date']")
    PO_STATUS = (By.XPATH, "//span[contains(text(),'PO Status')]")
    PO_NUMBER = (By.XPATH, "//span[contains(text(),'PO Number')]")
    BACK_ARROW = (By.XPATH, "//span[@role='img' and @aria-label='arrow-left']")
    BREADCRUMB = (By.XPATH,"//span[contains(@class,'breadcrumb')]//span")


class OrderManagement(BaseClass):

    def __init__(self,driver):
        self.driver=driver

    def validate_order_management_page(self):
            elements = self.get_webelements(Order_Endpoint.ORDER_MGMNT)
            checklist = ['orders' in self.driver.current_url, len(elements) > 1,
                         self.element_visible(Order_Endpoint.SEARCH_FILTER)]
            for index, value in enumerate(checklist):
                if not value:
                    print(f"Element at index {index} is False")
            assert not (False in checklist), " some element not present on Claim Management screen"


    def validate_searchfilter(self):
        self.clickOnButtonByText(' Search Filters')
        assert self.validatePresenceOfElementByText(' Add Search Criteria'),'Add Search Criteria not present'
        assert self.element_visible(Order_Endpoint.SEARCH_FILTER),'Search Filter not present'



    def validate_add_search_crieteria(self):
        self.click_element(Order_Endpoint.ADD_SEARCH)
        checklist = [self.validateDropDownHeadersByText('Field Name'),self.validateDropDownHeadersByText('Operator'),
                     self.validateDropDownHeadersByText('Value')]
        for index, value in enumerate(checklist):
            if not value:
                print(f"Element at index {index} == {checklist[index]} is False")
        assert not (False in checklist), "element not present on Claim Management screen"

    def select_data_for_orders_and_validate(self):
        self.wait_till_dropdown_clickable_and_select(Order_Endpoint.ENTITY,Order_Endpoint.Loc1,Order_Endpoint.Loc2,"Covered Entity")
        self.search_dropdown_and_select(Order_Endpoint.SEARCH_CE_NAME,Order_Endpoint.Loc1,Order_Endpoint.Loc2,"CE01")
        self.click_element(Order_Endpoint.APPLY_FILTER)
        checklist = [self.element_visible(Order_Endpoint.PHARMACY_NPI),self.element_visible(Order_Endpoint.WHOLESALER),
                     self.element_visible(Order_Endpoint.WHOLESALER_ACC),self.element_visible(Order_Endpoint.PO_NUMBER),
                     self.element_visible(Order_Endpoint.PO_STATUS)]
        for index, value in enumerate(checklist):
            if not value:
                print(f"Element at index {index} =={checklist[index]} is False")
        assert not (False in checklist), " element not present on Order Management screen"


    def validate_PO_details_screen(self):
        self.click_element(Order_Endpoint.PO_NUMBER_LINK)
        Order_Details_Present = self.get_text(Order_Endpoint.BREADCRUMB).lower() == "Order Details".lower()
        checklist = [('ORderDetails',Order_Details_Present), ('PO_Number',self.element_visible(Order_Endpoint.PO_NUMBER)),
                     ('PO_Status',self.element_visible(Order_Endpoint.PO_STATUS)),('Order_Creation date', self.element_visible(Order_Endpoint.ORDER_CREATION_DATE)),
                     ('Order Invoice',self.element_visible(Order_Endpoint.ORDER_INVOICE)), ('Order Akn',self.element_visible(Order_Endpoint.ORDER_AKN)),
                     ('Back_Arrow',self.element_visible(Order_Endpoint.BACK_ARROW))]
        for index, value in enumerate(checklist):
            if not value:
                print(f"Element at index {index} =={checklist[index]} is False")
        assert not (False in checklist), " element not present on order details screen"



