import os
import time
from sys import executable

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.ie.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjects.API_Pages import API_PAGES
from PageObjects.API_restbase import RestBaseClass
from PageObjects.UI_Pages import Pages
from TestData.CP_Test_Data import loginData


# driver = None


def pytest_addoption(parser):
    parser.addoption("--browser-name", action="store", default="chrome"
                     , help="Executing My Tests on Different Browsers")
    parser.addoption("--env-name", action="store", default="QA"
                     , help="Executing My Tests on Different Browsers")


@pytest.fixture(scope="module")
def ui(request):
    global driver
    try:
        directory = os.getcwd()
        env = request.config.getoption("--env-name")
        browser = request.config.getoption("--browser-name")
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_experimental_option("prefs", {"download.default_directory": directory + "\DownloadFiles"})
            # options.page_load_strategy = 'eager'
            # services = Service(executable_path=ChromeDriverManager().install())
            service = Service("C:\\Users\\Prajwal.Chunatkar\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
            driver = webdriver.Chrome(service=service,options=options)
            # driver.set_page_load_timeout(300)  # Increase the page load timeout
            driver.maximize_window()
            driver.delete_all_cookies()
        elif browser == "firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", directory + "\DownloadFiles")
            driver = webdriver.Firefox(executable_path=directory + "\\resources\\drivers\\geckodriver64.exe")
            driver = webdriver.Firefox(firefox_profile=profile)
        elif browser == "edge":
            # driver = webdriver.Ie(executable_path=directory + "\\resources\\drivers\\msedgedriver.exe")
            driver = webdriver.Edge()
        if env == "QA":
            driver.get("https://qa.equiscript.com/login")
            driver.refresh()
        elif env == "UAT":
            driver.get("https://uat.equiscript.com/login")
        ui_pages = Pages(driver)
        ui_pages.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
        ui_pages.login_page.switchto_homepage()
        yield ui_pages
    finally:
        if driver:
            driver.quit()
    # driver.quit()



# @pytest.fixture(scope="function")
# def rest(request):
@pytest.fixture(scope="module")
def login(ui):
    driver = ui
    ui_pages = Pages(driver)
    ui_pages.login_page.user_login(loginData.username, loginData.password, loginData.usernameMailinator)
    yield ui_pages

@pytest.fixture()
def rest():
    api = API_PAGES()
    yield api


