import datetime
import os
import inspect
import logging
import time
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from TestData.CP_Test_Data import emailNotification
import win32com.client


@pytest.mark.usefixtures("setup")
class BaseClass:

    def selectOptionByText(self, locator, Text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        select = Select(element)
        select.select_by_visible_text(Text)

    def selectOptionByValue(self, locator, value):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        select = Select(element)
        select.select_by_value(value)

    def selectOptionByIndex(self, locator, index):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        select = Select(element)
        select.select_by_index(index)

    def verify_element_present(self, locator, duration):
        wait = WebDriverWait(self.driver, duration)
        wait.until(EC.presence_of_element_located(locator))

    def switchChildwindow(self):
        childwindow = self.driver.window_handles[1]
        self.driver.switch_to.window(childwindow)
        print(self.driver.title)

    def switchParentWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def closeChildWindow(self):
        self.driver.close()

    def contextClick(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def doubleClick(self, locator):
        action = ActionChains(self.driver)
        action.double_click(locator).perform()

    def alertAccept(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def alertDismiss(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def alertText(self):
        alert = self.driver.switch_to.alert
        return alert.text

    def get_url(self, url):
        self.driver.get(url)

    def getscreenShot(self, fileName):
        self.driver.get_screenshot_as_file(fileName)

    # text may be frame id or frame name or index value
    def switch_to_iframe(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        self.driver.switch_to.frame(element)

    def defaultContent(self):
        self.driver.switch_to.default_content()

    def java_script_click(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    def get_text(self, locator):
        time.sleep(.5)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        return element.text

    def enabled(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        return element.is_enabled()

    def get_Attribute(self, locator):
        return locator.get_attribute("value")
        # driver.execute_script('return document.getElementsByName("name")[0].value')

    def refresh(self):
        """
        Refreshes the current page.

        :return: None
        """
        self.driver.refresh()
        time.sleep(1)

    def verify_field_is_marked_as_required(self, labelText, textOnField):
        """
        Will verify the given field label has an asterisk
        :param textOnField: Text on the label without the asterisk
        """
        formattedXpath = self._format_tuple(labelText, textOnField)
        text = self.driver.find_element(*formattedXpath).text
        assert text.endswith('*'), f'The field {textOnField} does not end with an *.'

    def click_and_hold_the_element(self, menuitem):
        """
            Clicks and hold the element.

            :return: None
        """
        text = self.driver.find_element(By.XPATH, "//a[contains(text(),'{}')]".format(menuitem))
        print('element is..', text)
        actionChains = ActionChains(self.driver)
        actionChains.click_and_hold(text).perform()

    def close_side_drawer_with_grey_area(self):
        """
        Closes the wide drawer by clicking the grey area.

        :return:
        """
        actionChains = ActionChains(self.driver)
        theElem = self.driver.find_element(By.CLASS_NAME, "app-name__text")
        actionChains.move_to_element(theElem).perform()
        actionChains.click(theElem).perform()

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(os.getcwd() + '\\logs\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def move_to_Element(self, locator):
        action = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located(locator))
        action.move_to_element(element).perform()

    def click_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        element.click()

    def click_element_by_moduleName(self, modulename):
        wait = WebDriverWait(self.driver, 10)
        xpath = f"//span[text()='{modulename}']"
        locator = (By.XPATH,xpath)
        element = wait.until(EC.presence_of_element_located(locator))
        element.click()

    def element_visible(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        status = element.is_displayed()
        return status

    def send_Keys(self, locator, value):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def get_attribute_value(self,locator,attribute):
        wait = WebDriverWait(self.driver,30)
        element = wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)

    def scroll_into_view(self, locator):
        # Run JavaScript to scroll until the element is in view
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def clear_input_text(self, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located(locator))
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)

    def action_send_keys(self, locator, value):
        action = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located(locator))
        element.click()
        action.send_keys(value).perform()

    def get_title(self):
        return self.driver.title

    def web_table_handle(self, tableRows, startRow, startColumn, locator1, locator2, username):
        wait = WebDriverWait(self.driver, 30)
        elements = wait.until(EC.presence_of_all_elements_located(tableRows))
        totalTableCount = len(elements)
        if totalTableCount == 1:
            totalTableCount = totalTableCount + 1
        print(totalTableCount)
        for i in range(startRow, totalTableCount):
            numberOfColumnsInRow = len(self.driver.find_elements(By.XPATH, locator1 + str(i) + locator2))
            time.sleep(1)
            for j in range(startColumn, numberOfColumnsInRow):
                web_element = self.driver.find_element(By.XPATH,
                                                       locator1 + str(i) + locator2 + "[" + str(j) + "]")
                content = web_element.text
                iframe = self.driver.find_element(By.ID, "html_msg_body")
                if content == emailNotification.login_otp_sub:
                    web_element.click()
                    time.sleep(2)
                    self.driver.switch_to.frame(iframe)
                    otp = self.driver.find_element(By.XPATH, "//table/tbody/tr/td/p[contains(.,'To log into the "
                                                             "application')]").text
                    new = str(otp)
                    new_otp = new.split()[14]
                    return new_otp
                elif content == emailNotification.reset_password_sub:
                    web_element.click()
                    time.sleep(.5)
                    self.driver.switch_to.frame(iframe)
                    reset_pwd_link = self.driver.find_element(By.XPATH, "//table/tbody/tr/td/p/a/following-sibling::a")
                    link = reset_pwd_link.text
                    time.sleep(.5)
                    return link
                elif content == emailNotification.app_locked_sub:
                    web_element.click()
                    time.sleep(.5)
                    self.driver.switch_to.frame(iframe)
                    reset_pwd_link = self.driver.find_element(By.XPATH, "//table/tbody/tr/td/p/a/following-sibling::a")
                    unlocked_link = reset_pwd_link.text
                    time.sleep(.5)
                    return unlocked_link
                elif content == emailNotification.forgot_password_sub:
                    web_element.click()
                    time.sleep(.5)
                    self.driver.switch_to.frame(iframe)
                    reset_pwd_link = self.driver.find_element(By.XPATH, "//table/tbody/tr/td/p/a/following-sibling::a")
                    forgot_password_link = reset_pwd_link.text
                    time.sleep(.5)
                    return forgot_password_link

    def search_user(self, tableRows, startRow, startColumn, locator1, locator2, username, email_id, useRole, status,
                    Type,termDate):

        totalTableCount = len(tableRows)
        if totalTableCount == 1:
            totalTableCount = totalTableCount + 1
        print(totalTableCount)
        for i in range(startRow, totalTableCount):
            numberOfColumnsInRow = len(self.driver.find_elements(By.XPATH, locator1 + str(i) + locator2))
            time.sleep(1)
            for j in range(startColumn, numberOfColumnsInRow):
                content = self.driver.find_element(By.XPATH,
                                                   locator1 + str(i) + locator2 + "[" + str(j) + "]").text
                if content == username:
                    if Type == "UserManagement":
                        email = self.driver.find_element(By.XPATH,
                                                         locator1 + str(i) + locator2 + "[" + str(
                                                             j + 3) + "]").text
                        user_role = self.driver.find_element(By.XPATH,
                                                             locator1 + str(i) + locator2 + "[" + str(
                                                                 j + 4) + "]").text
                        user_status = self.driver.find_element(By.XPATH,
                                                               locator1 + str(i) + locator2 + "[" + str(
                                                                   j + 7) + "]").text
                        assert email == email_id
                        assert user_role == useRole
                        assert user_status == status
                        break
                    if Type == "CoveredEntity":
                        covered_entity_type = self.driver.find_element(By.XPATH,
                                                                       locator1 + str(i) + locator2 + "[" + str(
                                                                           j + 1) + "]").text
                        live_date = self.driver.find_element(By.XPATH,
                                                             locator1 + str(i) + locator2 + "[" + str(
                                                                 j + 3) + "]").text
                        term_date = self.driver.find_element(By.XPATH,
                                                             locator1 + str(i) + locator2 + "[" + str(
                                                                 j + 4) + "]").text
                        ce_status = self.driver.find_element(By.XPATH,
                                                          locator1 + str(i) + locator2 + "[" + str(
                                                              j + 5) + "]").text

                        assert covered_entity_type == email_id
                        assert live_date == useRole
                        assert term_date==termDate
                        assert ce_status == status
                        break
                    if Type == "Pharmacies":
                        storeNumber = self.driver.find_element(By.XPATH,
                                                         locator1 + str(i) + locator2 + "[" + str(
                                                             j + 1) + "]").text
                        npi_number = self.driver.find_element(By.XPATH,
                                                             locator1 + str(i) + locator2 + "[" + str(
                                                                 j + 2) + "]").text
                        nabp_code = self.driver.find_element(By.XPATH,
                                                               locator1 + str(i) + locator2 + "[" + str(
                                                                   j + 3) + "]").text
                        assert storeNumber == email_id
                        assert npi_number == useRole
                        assert nabp_code == status
                        break

                    time.sleep(5)

    def click_dropdown(self, dropdownSelector, locator1, locator2, text):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located(dropdownSelector))
        element.click()
        # time.sleep(5)
        # self.driver.execute_script("arguments[0].click();", element)
        selectDropdown = (By.XPATH, locator1 + text + locator2)
        element1 = wait.until(EC.element_to_be_clickable(selectDropdown))
        time.sleep(.5)
        self.driver.execute_script("arguments[0].click();", element1)

    def read_email(self):
        time.sleep(45)
        outlook = win32com.client.Dispatch('outlook.application').GetNamespace("MAPI")
        inbox = outlook.Folders("Rajesh.Manchala@encora.com").Folders("Inbox")
        filter_mail = "[SenderEmailAddress] = 'manoj.cse08@gmail.com'" and "[Subject] = 'Your login verification - " \
                                                                           "One Time Password (OTP)'"
        messages = inbox.Items.Restrict(filter_mail)
        # messages.Restrict("[Subject] = 'Your login verification - One Time Password (OTP)'")
        messages.Sort("[ReceivedTime]", Descending=True)
        value = messages.GetFirst()
        otp = []
        if "Your login verification - One Time Password (OTP)" in str(value.Subject):
            new = str(value.Body)
            otp = new.split()[38]
        return otp

    def read_email_mailinator(self, username, total_rows, row, column, locator1, locator2, text):
        parentWindow = self.driver.current_window_handle
        self.driver.execute_script("window.open('https://www.mailinator.com/')")
        time.sleep(.2)
        childWindow = self.driver.window_handles
        for child in childWindow:
            if child != parentWindow:
                self.driver.switch_to.window(child)
                self.driver.maximize_window()
                time.sleep(2)
                self.driver.find_element(By.ID, "search").send_keys(username)
                self.driver.find_element(By.XPATH, "//button[text()='GO']").click()
                time.sleep(5)
                otp = self.web_table_handle(total_rows, row, column, locator1,
                                            locator2, text)
                self.driver.close()
                time.sleep(1)
                self.driver.switch_to.window(parentWindow)
                time.sleep(1)
                return otp

    def verify_page_nations_in_table(self):
        element = self.driver.find_element(By.XPATH,
                                           "//div[@class='ant-pagination-item-container']/ancestor::li/following"
                                           "-sibling::li/a")

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        numbers_of_rows = element.text
        for table_pages in range(1, int(numbers_of_rows)):
            self.driver.find_element(By.XPATH, "//li[@title='" + str(table_pages) + "']/a").click()
            time.sleep(2)

    def verify_table_page_nations_dropdowns(self):
        log = self.get_logger()
        wait = WebDriverWait(self.driver, 30)
        locator = (By.XPATH, "//span[@class='ant-select-selection-item']")
        element = wait.until(EC.presence_of_element_located(locator))
        element.click()
        time.sleep(1)
        locator1 = (By.XPATH, "//div[@class='ant-select-item-option-content']")
        elements_count = wait.until(EC.presence_of_all_elements_located(locator1))
        locator2 = (By.XPATH, "//table/tbody/tr")
        count = len(elements_count)
        for i in range(1, count + 1):
            Text = self.driver.find_element(By.XPATH,
                                            "(//div[@class='ant-select-item-option-content'])[" + str(i) + "]")
            time.sleep(2)
            print(Text.text)
            log.info(Text.text)
            time.sleep(2)
            Text.click()
            time.sleep(5)
            number_of_records = wait.until(EC.presence_of_all_elements_located(locator2))
            print(len(elements_count))
            time.sleep(2)
            element.click()

    def select_date(self, dateType, date):
        actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 30)
        locator1 = (By.XPATH, "//span[contains(text(),'" + dateType + "')]/parent::div/following-sibling::div"
                                                                      "/descendant::input")
        date_select = wait.until(EC.presence_of_element_located(locator1))
        self.clear_input_text(locator1)
        time.sleep(2)
        date_select.send_keys(date)
        time.sleep(2)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(1)

    def close_childwindow(self):
        parentWindow = self.driver.current_window_handle
        time.sleep(.2)
        childWindow = self.driver.window_handles
        for child in childWindow:
            if child != parentWindow:
                self.driver.switch_to.window(child)
                self.driver.close()
                time.sleep(2)
        self.driver.switch_to.window(parentWindow)
