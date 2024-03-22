import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.ExportCustomerDetailstoExcel import ExportCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_ExportSelectedCustomerInfoXlsx_007:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_exportSelectedCustomerInfoXlsx(self,setup):
        self.logger.info("****************** Export Selected Customer Info *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login Successful *************")

        self.logger.info("************** Starting Export Exported Customer Info to Xlsx file ******************")

        self.addcustm = AddCustomer(self.driver)
        self.addcustm.clickOnCustomersMenu()
        self.addcustm.clickOnCustomersMenuItem()
        self.logger.info("****************** Starting Customer Info Export *******************")

        cstminfo_export = ExportCustomer(self.driver)
        # self.xpath = selectCustomers(value)
        # checkbox = driver.find_element(By.XPATH, xpath)
        custm1 = cstminfo_export.selectCustomers(6)
        custm2 =cstminfo_export.selectCustomers(5)
        custm3 = cstminfo_export.selectCustomers(2)
        custm4 = cstminfo_export.selectCustomers(3)
        checkbox = self.driver.find_element(By.XPATH, custm1).click
        checkbox = self.driver.find_element(By.XPATH, custm2).click()
        checkbox = self.driver.find_element(By.XPATH, custm3).click()
        checkbox = self.driver.find_element(By.XPATH, custm4).click()

        cstminfo_export.clickOnExportbtn()
        cstminfo_export.exportSelectedCustomers()
        time.sleep(10)
        self.logger.info("********************* Test_ExportSelectedCustomerInfoXlsx_007 finished **********************")
        self.driver.close()