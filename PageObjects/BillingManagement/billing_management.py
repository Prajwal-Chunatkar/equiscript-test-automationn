from Utilities.BaseClass import BaseClass

class Billing(object):
    BILLING_MANAGEMENT = "//span[text()='Billing Management']"
    pass


class BillingManagement(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def verify_billing_management_page(self):
        elements = self.get_webelements(Billing.BILLING_MANAGEMENT)
        checklist = ['billing' in self.driver.current_url ,len(elements ) >1,
                     self.button_visible_bytext('Covered Entities'),self.button_visible_bytext('Pharmacies'),
                     self.button_visible_bytext(' Search Filters')]
        self.verify_table_headers("CE Name|OPA ID|Statement#|Billing Date|Billing Start Date|Billing End Date"
                                  "|Amount Due From PX($)|Admin Fee($)")
        assert not (False in checklist), " element not present on Claim Management screen"