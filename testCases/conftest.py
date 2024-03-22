import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
import os
location=os.getcwd()

preferences = {"download.default_directory":location}
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", preferences)


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge")
    else:
        driver = webdriver.Chrome(options=options)
    return driver

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request): # this will return the browser value to the setup method
    return request.config.getoption('--browser')

# pytest HTML reports
def pytest_html_report_title(report):
    report.title = "pytest Test Execution Report (nopCommerce)"

def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "nopCommerce"
    config.stash[metadata_key]["Module"] = "Customers"
    config.stash[metadata_key]["Tester"] = "Silas Francis"

def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
    metadata.pop('Packages', None)
    metadata.pop('Platform', None)


#pytest -s -v --html=Reports/report.html testCases/test_login_ddt.py --browser chrome
#pytest -s -v -n=2 --html=Reports/report.html testCases/test_login_ddt.py --browser chrome
#pytest -s -v -m "sanity" --html=Reports/report.html testCases/test_login_ddt.py --browser chrome
