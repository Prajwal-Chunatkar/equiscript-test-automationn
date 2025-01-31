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
    # global driver
    directory = os.getcwd()
    env = request.config.getoption("--env-name")
    browser = request.config.getoption("--browser-name")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"download.default_directory": directory + "\DownloadFiles"})
        services = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options,service=services)
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
        driver.get("https://cpframework-qa.excellarate.com/login")
    if env == "DEV":
        driver.get("http://192.168.5.30/ESQFATWeb/")

    driver.implicitly_wait(10)
    # request.cls.driver = driver
    driver = request.cls.driver
    yield
    driver.quit()

@pytest.fixture(scope="class")
def setup1(request):
    # global driver
    directory = os.getcwd()
    env = request.config.getoption("--env-name")
    browser = request.config.getoption("--browser-name")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"download.default_directory": directory + "\DownloadFiles"})
        services = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(chrome_options=options,service = services)
        driver.maximize_window()
        driver.delete_all_cookies()
    # elif browser == "firefox":
    #     profile = webdriver.FirefoxProfile()
    #     profile.set_preference("browser.download.folderList", 2)
    #     profile.set_preference("browser.download.manager.showWhenStarting", False)
    #     profile.set_preference("browser.download.dir", directory + "\DownloadFiles")
    #     # driver = webdriver.Firefox(executable_path=directory + "\\resources\\drivers\\geckodriver64.exe")
    #     driver = webdriver.Firefox(firefox_profile=profile)
    #     driver.maximize_window()
    # elif browser == "edge":
    #     # driver = webdriver.Ie(executable_path=directory + "\\resources\\drivers\\msedgedriver.exe")
    #     driver = webdriver.Edge()
    if env == "QA":
        driver.get("https://cpframework-qa.excellarate.com/login")
    if env == "DEV":
        driver.get("http://192.168.5.30/ESQFATWeb/")

    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.getcwd() + '\\reports\\report.html'
            file_name = report.nodeid.replace("::", "_") + str(int(round(time.time() * 1000))) + ".png"
            directory_file = os.path.join(report_directory, file_name)
            # capture_screenshot(directory_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
            report.extra = extra


# def capture_screenshot(name):
#     driver.get_screenshot_as_file(name)
#
#     allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
