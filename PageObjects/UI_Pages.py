from PageObjects.Analytics.analytics import Analytics
from PageObjects.BillingManagement.billing_management import BillingManagement
from PageObjects.ClaimManagementModule.claim_management import ClaimManagement
from PageObjects.HomePage import HomePage
from PageObjects.InventoryManagementModule.InventoryManagement import InventoryManagement
from PageObjects.LoginPage import LoginPage
from PageObjects.OrderManagementModule.OrderManagement import OrderManagement
from PageObjects.UserManagementModule.UserManagement.User_Management import UserManagement


class Pages(object):

    def __init__(self,driver):
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)
        self.claims = ClaimManagement(driver)
        self.user_management = UserManagement(driver)
        self.inventory_management = InventoryManagement(driver)
        self.ordermanagement = OrderManagement(driver)
        self.billing = BillingManagement(driver)
        self.analytics = Analytics(driver)
