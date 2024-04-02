# Testing nopCommerce Demo Application
This project involves the testing of the Customers Module on the nopCommerce Demo Platform using the Pytest FrameWork

## Features
- Page Object Model
- HTML Reports
- Data Driven Testing
- Logging
- Multiple Browsers Support
- Parallel Testing

## Test Scenarios
- Login into the nopCommerce demo site: https://admin-demo.nopcommerce.com/admin/
- Add New Customer
- Search For Customer
   - Search for Customer by Name
   - Search for Customer by ID
- Export Customers
     - Export All Customers
     - Export Selected Customers
- Login via test Data in xlsx file

## Languages, libraries and tools used
- Python
- Pytest
- pytest-html
- pytest-xdist
- Openpyxl
- Allure-pytest
- Pycharm

## Installation
To install the required libraries for distributed testing, run the following command in your terminal:
```bash
pip install -U pytest
pip install pytest-html
pip install pytest-xdist
pip install openpyxl
pip install allure-pytest
```

## Test Execution
Test Execution commands can be found in the run.bat file located in this respository 

#### Browser Supported:
- Chrome (--browser chrome)
- Edge (--browser edge)
- Firefox (--browser firefox)
  
```bash
e.g.
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
```
> This will run test on Chrome Browser

> If no browser is specified tests will be executed on chrome
