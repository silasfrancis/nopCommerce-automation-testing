from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExportCustomer:
    drpExport_xpath = "//button[@class='btn btn-success dropdown-toggle']"
    exportAllCustomers = "//li[@class='dropdown-item']//button[@name='exportexcel-all']"
    exportSelectedCustomers = "//li[@class='dropdown-item']//button[@id='exportexcel-selected']"
    customer_checkboxes_xpath = "//td//input[@name='checkbox_customers']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody//tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody//tr//td"


    def __init__(self, driver):
        self.driver = driver

    def clickOnExportbtn(self):
        self.driver.find_element(By.XPATH, self.drpExport_xpath).click()

    def exportAllCustomers(self):
        export_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='dropdown-item']//button[@name='exportexcel-all']"))
        )
        export_button.click()

    def exportSelectedCustomers(self):
        export_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='dropdown-item']//button[@id='exportexcel-selected']"))
        )
        export_button.click()


    def selectCustomers(self, value):
        return f"//td//input[@name='checkbox_customers' and @value='{value}']"
        #driver.find_elements(By.CSS_SELECTOR, "td input[name='checkbox_customers'][value='6,5,2,3']").click()







