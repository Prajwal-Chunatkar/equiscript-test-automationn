import time

from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass


class LoginPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    ENTER_OTP = (By.XPATH, "//div/child::input")
    FAILED_TEXT = (By.XPATH, "//div[contains(@class,'message-notice-content')]//span[2]")
    TOTAL_ROWS = (By.XPATH, "//div[@class='os-content']/table/tbody/tr")
    MAIL_SINGLE_ROW = "//div[@class='os-content']/table/tbody/tr["
    MAIL_SINGLE_COLUMN = "]/td"
    SINGLE_ROW = "//table/tbody/tr["
    SINGLE_COLUMN = "]/td"
    LOGOUT_DOWN_ARROW = (By.XPATH, "//a[contains(@class,'dropdown')]")


    def get_total_rows(self):
        return self.driver.find_elements(*LoginPage.TOTAL_ROWS)

    def user_lock_login(self, username, password):
        self.text_element_visible('Contract Pharmacy')
        self.text_element_visible('Welcome!')
        self.text_element_visible('Sign in')
        self.button_visible_bytext('Login')
        self.send_Keys_ByTitle('Username', username)
        self.send_Keys_ByTitle('Password', password)
        self.click_button_bytext('Login')

    def user_login(self, username, password, otpmailid):
        title = self.get_title()
        assert title.lower() == "PATIENT FIRST".lower()
        self.text_element_visible('Welcome!')
        self.text_element_visible('Sign in')
        self.button_visible_bytext('Login')
        self.send_Keys_ByTitle('Username',username)
        self.send_Keys_ByTitle('Password',password)
        self.click_button_bytext('Login')
        text = self.get_otp_popup_text()
        # if not text=="A One Time Password has been sent to your registered Email ID":
        #     self.otp_sent_failed(text,username)
        #     return
        # self.verify_popup_present_ByText('A One Time Password has been sent to your registered Email ID', 60)
        # text = self.get_popup_text('A One Time Password has been sent to your registered Email ID')
        assert text == "A One Time Password has been sent to your registered Email ID",f"OTP message pop-up {text}"
        otp = self.read_email_mailinator(otpmailid, self.TOTAL_ROWS, 1, 1, LoginPage.MAIL_SINGLE_ROW,
                                         LoginPage.MAIL_SINGLE_COLUMN, "Your login verification - One "
                                                                       "Time Password (OTP)")
        print(otp)
        if text == 'A One Time Password has been sent to your registered Email ID':
            self.enter_otp(otp)
        self.click_button_bytext('Verify')
        time.sleep(2)

    def otp_sent_failed(self,text,username):
        try:
            # self.verify_popup_present_ByText('Unable to send mail this time, please try again later!', 5)
            # text = self.get_popup_text('Unable to send mail this time, please try again later!')
            # text = self.get_otp_popup_text()
            otp_failed = text == "Unable to send mail this time, please try again later!"
            if otp_failed:
                self.enter_otp(username)
                self.click_button_bytext('Verify')
            return otp_failed
        except Exception as e:
            print(f"OTP sent success {e}")

    def enter_otp(self,otp):
        self.driver.find_element(By.XPATH, "//div/child::input[1]").send_keys(otp[0])
        self.driver.find_element(By.XPATH, "//div/child::input[2]").send_keys(otp[1])
        self.driver.find_element(By.XPATH, "//div/child::input[3]").send_keys(otp[2])
        self.driver.find_element(By.XPATH, "//div/child::input[4]").send_keys(otp[3])
        self.driver.find_element(By.XPATH, "//div/child::input[5]").send_keys(otp[4])
        self.driver.find_element(By.XPATH, "//div/child::input[6]").send_keys(otp[5])


    def user_logout(self):
        time.sleep(2)
        self.verify_element_present(self.LOGOUT_DOWN_ARROW, 30)
        # self.move_to_Element(self.LOGOUT_DOWN_ARROW)
        self.click_element(self.LOGOUT_DOWN_ARROW)
        self.move_to_Element(self.LOGOUT_DOWN_ARROW)
        time.sleep(.5)
        self.click_element_bytext('Logout')
        self.verify_element_present_bytitle('username', 30)

    def newuser_login_and_logout(self, username, password, otpmailid):
        title = self.get_title()
        assert title.lower() == "PATIENT FIRST".lower()
        self.text_element_visible('Welcome!')
        self.text_element_visible('Sign in')
        self.button_visible_bytext('Login')
        self.send_Keys_ByTitle('Username', username)
        self.send_Keys_ByTitle('Password', password)
        self.click_button_bytext('Login')
        text = self.get_otp_popup_text()
        if self.otp_sent_failed(text,username):
            return
        self.verify_popup_present_ByText('A One Time Password has been sent to your registered Email ID', 60)
        text = self.get_popup_text('A One Time Password has been sent to your registered Email ID')
        assert text == "A One Time Password has been sent to your registered Email ID"
        # self.verify_element_present(self.OTP_TEXT, 30)
        # otp = []
        otp = self.read_email_mailinator(otpmailid, self.TOTAL_ROWS, 1, 1, LoginPage.MAIL_SINGLE_ROW,
                                         LoginPage.MAIL_SINGLE_COLUMN, "Your login verification - One "
                                                                       "Time Password (OTP)")
        parentWindow = self.driver.current_window_handle
        print(otp)
        if text == 'A One Time Password has been sent to your registered Email ID':
            self.enter_otp(otp)
        self.click_button_bytext('Verify')
        time.sleep(2)
        childWindow = self.driver.window_handles
        for child in childWindow:
            if child != parentWindow:
                self.driver.switch_to.window(child)
        self.user_logout()

    def switchto_homepage(self):
        parentWindow = self.driver.current_window_handle
        time.sleep(.2)
        childWindow = self.driver.window_handles
        for child in childWindow:
            if child != parentWindow:
                self.driver.switch_to.window(child)

