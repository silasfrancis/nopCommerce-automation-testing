from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tbl_SearchResults_xpath = "//div[@class='dataTables_scrollHeadInner']//table[@class='table table-bordered table-hover table-striped dataTable no-footer']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody//tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody//tr//td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoRows(self):
        table_element = self.driver.find_element(By.XPATH, self.tableRows_xpath)
        return len(table_element.find_elements(By.TAG_NAME, "tr"))
        #return len(self.driver.find_element(By.XPATH, self.tableRows_xpath))

    def getNoColomns(self):
        table_element = self.driver.find_element(By.XPATH, self.tableColumns_xpath)
        return len(table_element.find_elements(By.TAG_NAME, "td"))
        # return len(self.driver.find_element(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        for r in range(1, self.getNoRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody//tr["+str(r)+"]//td[2]").text
            if emailid == email:
                assert True
                break
        return False


    def searchCustomerByName(self, Name):
        for r in range (1, self.getNoRows()+1):
            try:
                table = self.driver.find_element(By.XPATH, self.table_xpath)
                name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody//tr["+str(r)+"]//td[3]").text
                if name == Name:
                    return True
            except NoSuchElementException:
                pass
        return False

