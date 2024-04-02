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
### 1. Tests could be executed by running the following commands:
#### Chrome Browser:
```bash
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome
pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases --browser chrome
pytest -s -v -m "regression" --html=./Reports/report.html testCases --browser chrome
```
#### Edge: 
```bash
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser edge
pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser edge
pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases --browser edge
pytest -s -v -m "regression" --html=./Reports/report.html testCases --browser edge
```
#### Firefox: 
```
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser firefox
pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser firefox
pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases --browser firefox
pytest -s -v -m "regression" --html=./Reports/report.html testCases --browser firefox
```
### 2. Running the Batch File located in this directory:
   Test can also be executed by running the batch file located in this directory.
   Double click on in or switch directory to this directory on command prompt and run the batch file from there
   - N/B: The batch file will run on default browser for now, but can be edited .
   



