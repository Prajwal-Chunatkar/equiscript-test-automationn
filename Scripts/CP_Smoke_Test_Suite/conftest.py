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

# driver = None


def pytest_addoption(parser):
    parser.addoption("--browser-name", action="store", default="chrome"
                     , help="Executing My Tests on Different Browsers")
    parser.addoption("--env-name", action="store", default="QA"
                     , help="Executing My Tests on Different Browsers")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    directory = os.getcwd()
    env = request.config.getoption("--env-name")
    browser = request.config.getoption("--browser-name")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"download.default_directory": directory + "\DownloadFiles"})
        # services = Service(executable_path=ChromeDriverManager().install())
        service = Service("C:\\Users\\Prajwal.Chunatkar\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=service,options=options)
        driver.maximize_window()
        driver.delete_all_cookies()
    elif browser == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", directory + "\DownloadFiles")
        # driver = webdriver.Firefox(executable_path=directory + "\\resources\\drivers\\geckodriver64.exe")
        driver = webdriver.Firefox(firefox_profile=profile)
        driver.maximize_window()
    elif browser == "edge":
        # driver = webdriver.Ie(executable_path=directory + "\\resources\\drivers\\msedgedriver.exe")
        driver = webdriver.Edge()
    if env == "QA":
        driver.get("https://qa.equiscript.com/")
    if env == "DEV":
        driver.get("http://192.168.5.30/ESQFATWeb/")

    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()


