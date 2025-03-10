from Utilities.BaseClass import BaseClass


class Analytics_Endpoints(object):
    ANALYTICS = "//span[text()='Analytics']"
    pass


class Analytics(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def verify_analytics_page(self):
        elements = self.get_webelements(Analytics_Endpoints.ANALYTICS)
        checklist = ['analytics' in self.driver.current_url, len(elements) > 1,
                     self.verify_element_present_bytext('Audit Report',10),self.verify_element_present_bytext('Invoiced Claims Detailed Report (Pharmacy)',10),
                     self.verify_element_present_bytext('Performance Report (CE)',10),self.verify_element_present_bytext('Non Captured Claims Report',10),
                     self.verify_element_present_bytext('Gateway Reports',10),self.verify_element_present_bytext('340B ESP Report',10),
                     self.verify_element_present_bytext('Unreplenished Claims Report for RBB Pharmacies/CE’s',10)]
        assert not (False in checklist), " element not present on Claim Management screen"