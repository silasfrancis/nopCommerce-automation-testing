import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.ExportCustomerDetailstoExcel import ExportCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_ExportAllCustomerInfoXlsx_006:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_exportAllCustomerInfoXlsx(self,setup):
        self.logger.info("****************** Export All Customer Info *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login Successful *************")

        self.logger.info("************** Starting Export All Customer Info to Xlsx file ******************")

        self.addcustm = AddCustomer(self.driver)
        self.addcustm.clickOnCustomersMenu()
        self.addcustm.clickOnCustomersMenuItem()

        self.logger.info("****************** Starting All Customer Info Export *******************")

        exportCustInfo = ExportCustomer(self.driver)
        exportCustInfo.clickOnExportbtn()
        exportCustInfo.exportAllCustomers()
        time.sleep(10)
        self.logger.info("********************* Test_ExportAllCustomerInfoXlsx_006 finished **********************")
        self.driver.close()




