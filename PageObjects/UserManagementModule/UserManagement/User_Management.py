import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from TestData.CP_Test_Data import emailNotification

from Utilities.BaseClass import BaseClass
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC


class UserManagement(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    CONFIGURATION_MANAGEMENT = (By.XPATH, "//span[text()='Configuration Management']")
    USER_MANAGEMENT_TAB = (By.XPATH, "//span[text()='User Management']")
    ADD_USER_BUTTON = (By.XPATH, "//span[contains(text(),'Add User')]/parent::button")
    CONTINUE = (By.XPATH, "//span[text()='Continue']")
    CONFIRM = (By.XPATH, "//span[text()='Confirm']")
    USER_ROLE = (By.ID, "addce_userRole")
    FIRST_NAME = (By.ID, "addce_firstName")
    LAST_NAME = (By.ID, "addce_lastName")
    EMAIL_ID = (By.ID, "addce_emailId")
    CANCEL_BUTTON = (By.XPATH, "//span[text()='Cancel']")
    ENTITY_ACCESS_TAB = (By.ID, "rc-tabs-0-tab-1")
    ROLE_PERMISSION_TAB = (By.ID, "rc-tabs-0-tab-2")
    SAVE_NEXT_BUTTON = (By.XPATH, "//span[contains(text(),'Save & Next')]")
    SAVE_CONTINUE = (By.XPATH, "//span[contains(text(),'Save & Continue')]")
    USER_ADDED_SUCCESSFULLY = (By.XPATH, "//span[text()='New User is successfully added!']")
    GO_TO_USER_LIST = (By.XPATH, "//span[text()='Go to User List']")
    LOCATOR1 = "//div[contains(text(),'"
    LOCATOR2 = "')]"
    ADD_USER_SETTINGS = (By.XPATH, "//span[text()='Add User Settings']")
    CONFIRM_BUTTON = (By.XPATH, "//span[text()='Confirm']")
    SECURITY_QUESTION1 = (By.ID, "register_selectedsq1")
    SECURITY_QUESTION2 = (By.ID, "register_selectedsq2")
    SET_THE_FOLLOWING_SECURITY_QUESTIONS_LABEL = (By.XPATH, "//strong[text()='Set the following Security Questions']")
    SECURITY_ANSWER1 = (By.ID, "register_sq1")
    SECURITY_ANSWER2 = (By.ID, "register_sq2")
    CREATE_PASSWORD_SECTION = (By.XPATH, "//strong[text()='Create your Password']")
    REGISTER_PASSWORD = (By.ID, "register_pwd")
    CONFIRM_PASSWORD = (By.ID, "register_cpwd")
    SAVE_BUTTON = (By.XPATH, "//span[text()='Save']")
    SEARCH_HERE = (By.XPATH, "//input[@placeholder='Search here']")
    # Edit Page
    EDIT_BUTTON = (By.XPATH, "//span[text()='Edit']")
    EMAIL_ID_IN_EDIT_PAGE = (By.ID, "addce_emailId")
    USER_ROLE_IN_EDIT_PAGE = (By.ID, "addce_roleId")
    FIRST_NAME_IN_EDIT_PAGE = (By.ID, "addce_firstName")
    LAST_NAME_IN_EDIT_PAGE = (By.ID, "addce_lastName")
    USER_EDIT_SUCCESSFULLY = (By.XPATH, "// span[contains(text(), 'User edit  successfully done')]")
    DETAILS_UPDATED_SUCCESSFULLY = (By.XPATH, "//span[text()='Details updated successfully!']")
    # View Page
    VIEW_SYMBOL = (By.XPATH, "//table/tbody/tr/td[1]/span")
    USER_DETAILS = (By.XPATH, "//span[contains(text(),'User Details')]")
    # User Details Page
    USER = (By.XPATH, "//span[text()='User Name']/parent::div/following-sibling::div")
    FIRSTNAME = (By.XPATH, "//span[text()='First Name']/parent::div/following-sibling::div")
    LASTNAME = (By.XPATH, "//span[text()='Last Name']/parent::div/following-sibling::div")
    EMAILID = (By.XPATH, "//span[text()='Email ID']/parent::div/following-sibling::div")
    ACCOUNT = (By.XPATH, "//span[text()='Account']/parent::div/following-sibling::div")
    REQUEST = (By.XPATH, "//span[text()='Request']/parent::div/following-sibling::div")
    STATUS = (By.XPATH, "//span[text()='Status']/parent::div/following-sibling::div")
    USERROLE = (By.XPATH, "//span[text()='User Role']/parent::div/following-sibling::div")
    # Change Password Page
    CHANGE_PASSWORD_SECURITY_Q1 = (By.ID, "normal_login_answer1")
    CHANGE_PASSWORD_SECURITY_Q2 = (By.ID, "normal_login_answer2")
    VALIDATE_ANSWERS = (By.XPATH, "//span[text()='Validate Answers']")
    PASSWORD_IN_CHANGE_PASSWORD_PAGE = (By.ID, "normal_login_password")
    CONFIRM_PASSWORD_IN_CHANGE_PASSWORD_PAGE = (By.ID, "normal_login_confirmpassword")
    # Forgot Password Page
    ENTER_EMAIL_ID = (By.ID, "normal_login_email")
    SUBMIT_BUTTON = (By.XPATH, "//span[text()='Submit']")
    EMAIL_SENT_TO_EMAIL_ID = (By.XPATH, "//span[text()='Password reset link sent to your registered email ID.']")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Password?")
    ADD_NEW_USER_PAGE = (By.XPATH, "//span[text()='Add New User']")
    VIEW_OPTION = (By.XPATH, "(//table/tbody/tr/td/span)[1]")
    DOT_OPTIONS = (By.XPATH, "//table/tbody/tr[1]/td/button/span")
    USERNAME_VALUE = (By.XPATH,"//input[@name='userName']")

    def edit_button(self, username):
        return self.driver.find_element(By.XPATH,
                                        "//table/tbody/tr[1]/td/span[text()='" + username + "']/parent::td/following-sibling::td/button/span")

    def get_user_details(self, attribute):
        return self.driver.find_element(By.XPATH,
                                        "//span[text()='" + attribute + "']/parent::div/following-sibling::div")

    def user_navigation(self):
        self.verify_element_present(self.USER_MANAGEMENT_TAB, 30)
        self.click_element(self.USER_MANAGEMENT_TAB)
        self.verify_element_present(self.ADD_USER_BUTTON, 20)
        self.click_element(self.ADD_USER_BUTTON)
        self.verify_element_present(self.ADD_NEW_USER_PAGE, 20)
        status = self.element_visible(self.ADD_NEW_USER_PAGE)
        assert status == True

    def verify_edit_button_in_table(self):
        self.verify_element_present(self.USER_MANAGEMENT_TAB, 20)
        self.click_element(self.USER_MANAGEMENT_TAB)
        self.move_to_Element(self.DOT_OPTIONS)
        self.click_element(self.DOT_OPTIONS)
        time.sleep(2)
        status = self.element_visible(self.EDIT_BUTTON)
        assert status == True
        time.sleep(2)
        self.click_element(self.USER_MANAGEMENT_TAB)

    def um_table_page_nation_dropdowns(self):
        self.verify_element_present(self.USER_MANAGEMENT_TAB, 30)
        self.click_element(self.USER_MANAGEMENT_TAB)
        self.verify_table_page_nations_dropdowns()
        time.sleep(5)

    def um_table_page_nations(self):
        self.refresh()
        time.sleep(2)
        self.verify_element_present(self.USER_MANAGEMENT_TAB, 20)
        time.sleep(2)
        self.click_element(self.USER_MANAGEMENT_TAB)
        self.verify_page_nations_in_table()

    def set_password(self, question1, question2, answer1, answer2, password):
        self.verify_element_present(self.SET_THE_FOLLOWING_SECURITY_QUESTIONS_LABEL, 30)
        self.click_dropdown(self.SECURITY_QUESTION1, UserManagement.LOCATOR1, UserManagement.LOCATOR2, question1)
        self.send_Keys(self.SECURITY_ANSWER1, answer1)
        time.sleep(2)
        self.click_element(self.SECURITY_QUESTION2)
        self.driver.implicitly_wait(1)
        button = self.driver.find_element(By.XPATH, "(//div[contains(text(),'" + question2 + "')])[2]")
        button.click()
        self.send_Keys(self.SECURITY_ANSWER2, answer2)
        self.verify_element_present(self.CREATE_PASSWORD_SECTION, 5)
        self.send_Keys(self.REGISTER_PASSWORD, password)
        self.send_Keys(self.CONFIRM_PASSWORD, password)
        self.click_element(self.SAVE_BUTTON)
        self.verify_element_present(LoginPage.USERNAME, 30)

    def add_user(self, role, firstname, lastname, email, question1, question2, answer1, answer2, password):
        login_page = LoginPage(self.driver)
        logs = self.get_logger()
        self.verify_element_present(self.USER_MANAGEMENT_TAB, 30)
        time.sleep(.5)
        self.click_element(self.USER_MANAGEMENT_TAB)
        self.element_visible(self.ADD_USER_BUTTON)
        self.click_element(self.ADD_USER_BUTTON)
        self.click_dropdown(self.USER_ROLE, UserManagement.LOCATOR1, UserManagement.LOCATOR2, role)
        self.send_Keys(self.FIRST_NAME, firstname)
        self.send_Keys(self.LAST_NAME, lastname)
        time.sleep(2)
        self.send_Keys(self.EMAIL_ID, email)
        username = self.get_attribute_value(self.USERNAME_VALUE,"value")
        self.click_element(self.CONTINUE)
        time.sleep(5)
        self.click_element(self.CONFIRM)
        # self.click_element(self.ADD_USER_BUTTON)
        # self.verify_element_present(self.SAVE_NEXT_BUTTON, 30)
        # time.sleep(.1)
        # self.java_script_click(self.SAVE_NEXT_BUTTON)
        text = self.get_text(self.USER_ADDED_SUCCESSFULLY)
        assert text == 'New User is successfully added!'
        # self.click_element(self.CONFIRM_BUTTON)
        time.sleep(2)
        self.verify_element_present(self.GO_TO_USER_LIST, 20)
        self.click_element(self.GO_TO_USER_LIST)
        self.verify_element_present(self.ADD_USER_BUTTON, 10)
        print("email:" + email)
        logs.info("email:" + email)
        login_page.user_logout()
        # self.driver.close()
        self.close_childwindow()
        reset_password_link = self.read_email_mailinator(email, LoginPage.TOTAL_ROWS, 1, 1, LoginPage.MAIL_SINGLE_ROW,
                                                         LoginPage.MAIL_SINGLE_COLUMN,
                                                         emailNotification.reset_password_sub)
        logs.info(reset_password_link)
        parentWindow = self.driver.current_window_handle
        self.driver.execute_script("window.open('" + reset_password_link + "')")
        childWindow = self.driver.window_handles
        for child in childWindow:
            if child != parentWindow:
                self.driver.switch_to.window(child)
                self.driver.maximize_window()
                self.set_password(question1, question2, answer1, answer2, password)
                time.sleep(2)
                self.driver.close()
                time.sleep(1)
                self.driver.switch_to.window(parentWindow)
                time.sleep(1)
        return username

    def search_new_user(self, username, email, userRole):
        log = self.get_logger()
        self.click_element(self.USER_MANAGEMENT_TAB)
        self.send_Keys(self.SEARCH_HERE, username)
        self.search_user(LoginPage.TOTAL_ROWS, 1, 1, LoginPage.SINGLE_ROW, LoginPage.SINGLE_COLUMN, username, email,
                         userRole, 'Active', "UserManagement", "")
        log.info(username)

    def edit_user(self, username, newFirstName, newLastName):
        actions = ActionChains(self.driver)
        log = self.get_logger()
        self.verify_element_present(self.USER_MANAGEMENT_TAB, 20)
        self.click_element(self.USER_MANAGEMENT_TAB)
        self.verify_element_present(self.SEARCH_HERE, 20)
        self.send_Keys(self.SEARCH_HERE, username)
        time.sleep(5)
        element = self.edit_button(username)
        actions.move_to_element(element).perform()
        self.verify_element_present(self.EDIT_BUTTON, 10)
        time.sleep(2)
        self.click_element(self.EDIT_BUTTON)
        time.sleep(2)
        self.verify_element_present(self.EMAIL_ID_IN_EDIT_PAGE, 30)
        disabled_user_role_field = self.enabled(self.USER_ROLE_IN_EDIT_PAGE)
        disabled_email_field = self.enabled(self.EMAIL_ID_IN_EDIT_PAGE)
        log.info(disabled_email_field)
        log.info(disabled_user_role_field)
        assert False == disabled_user_role_field
        assert False == disabled_email_field
        firstname = self.driver.find_element(By.ID, "addce_firstName")
        lastname = self.driver.find_element(By.ID, "addce_lastName")
        self.enabled(self.FIRST_NAME_IN_EDIT_PAGE)
        self.scroll_into_view(self.SAVE_CONTINUE)
        if newFirstName != "":
            self.clear_input_text(self.FIRST_NAME_IN_EDIT_PAGE)
            firstname.send_keys(newFirstName)
        if newLastName != "":
            self.clear_input_text(self.LAST_NAME_IN_EDIT_PAGE)
            lastname.send_keys(newLastName)
        self.verify_element_present(self.SAVE_CONTINUE, 30)
        time.sleep(2)
        self.click_element(self.SAVE_CONTINUE)
        self.verify_element_present(self.DETAILS_UPDATED_SUCCESSFULLY, 10)
        details_updated_successfully = self.get_text(self.DETAILS_UPDATED_SUCCESSFULLY)
        assert details_updated_successfully == "Details updated successfully!"
        self.click_element(self.SAVE_NEXT_BUTTON)
        self.verify_element_present(self.CONFIRM_BUTTON, 10)
        self.click_element(self.CONFIRM_BUTTON)
        self.verify_element_present(self.USER_EDIT_SUCCESSFULLY, 20)
        user_edit_successfully = self.get_text(self.USER_EDIT_SUCCESSFULLY)
        print(user_edit_successfully)
        assert user_edit_successfully == "User edit successfully done"
        self.element_visible(self.GO_TO_USER_LIST)
        self.click_element(self.GO_TO_USER_LIST)
        self.verify_element_present(self.ADD_USER_BUTTON, 20)
        time.sleep(2)

    def view_user(self, username, accountStatus, Status, userRole):
        log = self.get_logger()
        self.verify_element_present(self.CONFIGURATION_MANAGEMENT, 20)
        self.click_element(self.CONFIGURATION_MANAGEMENT)
        time.sleep(2)
        self.click_element(self.USER_MANAGEMENT_TAB)
        self.verify_element_present(self.SEARCH_HERE, 20)
        self.send_Keys(self.SEARCH_HERE, username)
        self.click_element(self.VIEW_SYMBOL)
        self.verify_element_present(self.USER_DETAILS, 20)
        user_name = self.get_text(self.USER)
        log.info(user_name)
        assert user_name == username
        self.element_visible(self.FIRSTNAME)
        self.element_visible(self.LASTNAME)
        self.element_visible(self.EMAILID)
        account = self.get_text(self.ACCOUNT)
        log.info(account)
        assert account == accountStatus
        self.element_visible(self.REQUEST)
        status = self.get_text(self.STATUS)
        log.info(status)
        assert status == Status
        user_role = self.get_text(self.USERROLE)
        assert user_role == userRole
        log.info(user_role)

    def forgot_password(self, email):
        self.verify_element_present(self.FORGOT_PASSWORD_LINK, 30)
        self.click_element(self.FORGOT_PASSWORD_LINK)
        self.verify_element_present(self.ENTER_EMAIL_ID, 20)
        self.send_Keys(self.ENTER_EMAIL_ID, email)
        self.element_visible(self.SUBMIT_BUTTON)
        self.click_element(self.SUBMIT_BUTTON)
        self.verify_element_present(self.EMAIL_SENT_TO_EMAIL_ID, 30)
        alert_text = self.get_text(self.EMAIL_SENT_TO_EMAIL_ID)
        assert alert_text == 'Password reset link sent to your registered email ID.'

    def unlock_user(self, email, answer1, answer2, password, Type):
        login_page = LoginPage(self.driver)
        reset_password_link = self.read_email_mailinator(email, LoginPage.TOTAL_ROWS, 1, 1, LoginPage.MAIL_SINGLE_ROW,
                                                         LoginPage.MAIL_SINGLE_COLUMN,
                                                         Type)
        parentWindow = self.driver.current_window_handle
        self.driver.execute_script("window.open('" + reset_password_link + "')")
        childWindow = self.driver.window_handles
        for child in childWindow:
            if child != parentWindow:
                self.driver.switch_to.window(child)
                self.driver.maximize_window()
                self.verify_element_present(self.CHANGE_PASSWORD_SECURITY_Q1, 30, )
                self.send_Keys(self.CHANGE_PASSWORD_SECURITY_Q1, answer1)
                self.send_Keys(self.CHANGE_PASSWORD_SECURITY_Q2, answer2)
                self.click_element(self.VALIDATE_ANSWERS)
                self.verify_element_present(self.PASSWORD_IN_CHANGE_PASSWORD_PAGE, 30)
                self.send_Keys(self.PASSWORD_IN_CHANGE_PASSWORD_PAGE, password)
                self.send_Keys(self.CONFIRM_PASSWORD_IN_CHANGE_PASSWORD_PAGE, password)
                self.click_element(self.SAVE_BUTTON)
                self.verify_element_present(login_page.USERNAME, 30)
                time.sleep(2)
                self.driver.close()
                time.sleep(1)
                self.driver.switch_to.window(parentWindow)
                time.sleep(1)
