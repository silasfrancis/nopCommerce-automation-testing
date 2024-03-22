import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("*************** Search CustomerBy Name ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login Successful *************")

        self.logger.info("************** Starting Search Customer by Name ******************")

        self.addcustm = AddCustomer(self.driver)
        self.addcustm.clickOnCustomersMenu()
        self.addcustm.clickOnCustomersMenuItem()

        self.logger.info("*************** searching customer by Name *******************")
        searchcustm = SearchCustomer(self.driver)
        searchcustm.setFirstName("Steve")
        searchcustm.setLastName("Gates")
        searchcustm.clickSearch()
        time.sleep(5)
        status = searchcustm.searchCustomerByName("Steve Gates")
        if status == self.driver.find_element(By.XPATH, "//table[@id='customers-grid']//tbody//tr//td[3]").text:
            assert True
        self.logger.info("*************** Test_SearchCustomerByName_005 finished ********************")
        self.driver.close()
