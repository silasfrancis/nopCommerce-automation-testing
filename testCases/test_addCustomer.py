import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self, setup):
        self.logger.info('*********** Test_003_AddCustomer ************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('************ Login Successful ************')

        self.logger.info('************ Starting Add Customer Test **************')

        self.addcstm = AddCustomer(self.driver)
        self.addcstm.clickOnCustomersMenu()
        self.addcstm.clickOnCustomersMenuItem()

        self.addcstm.clickOnAddnew()

        self.logger.info('************ Providing Customer Info ************')

        random_username = ''.join(random.choices(string.ascii_lowercase+string.digits, k=8))
        self.email = random_username + "@gmail.com"

        self.addcstm.setEmail(self.email)
        self.addcstm.setPassword("testing123")
        self.addcstm.setCustomerRoles('Guests')
        self.addcstm.setManagerOfVendor('Vendor 2')
        self.addcstm.setGender('Male')
        self.addcstm.setFirsName('Francis')
        self.addcstm.setLastname('Silas')
        self.addcstm.setDob('7/05/2002')
        self.addcstm.setCompanyName('SilasQA')
        self.addcstm.setAdminContent('This is for software testing.......')
        self.addcstm.clickOnSave()

        self.logger.info('************ Saving Customer Info *************')

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info('********** Add Customer Test Passed ************')
        else:
            self.driver.save_screenshot("\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error('************** Add Customer Test Failed **************')
            assert False

        self.driver.close()
        self.logger.info('********** Ending Test_003 Add Customer Test **********')



