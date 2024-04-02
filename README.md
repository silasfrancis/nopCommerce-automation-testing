# Testing nopCommerce Demo Application
This project involves the testing of the Customers Module on the nopCommerce Demo Platform using the Pytest FrameWork

Features
Page Object Model
HTML Reports
Data Driven Testing
Multiple Browsers Support
Parallel Testing

*insert test execution video here*
*insert html report*

Languages, libraries and tools used
Python
Pytest
pytest-html
pytest-xdist
Openpyxl
Allure-pytest
Pycharm

Installation
Install the dependencies to excute the testCases

Install Pytest:
pip install -U pytest

install pytest-html: 
pip install pytest-html

install pytest-xdist
pip install pytest-xdist

install openpyxl: 
pip install openpyxl

install allure-pytest:
pip install allure-pytest

Test Execution
1. Tests could be executed by running the following commands:
Chrome Browser:
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome
pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases --browser chrome
pytest -s -v -m "regression" --html=./Reports/report.html testCases --browser chrome

Edge: 
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser edge
pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser edge
pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases --browser edge
pytest -s -v -m "regression" --html=./Reports/report.html testCases --browser edge

Firefox: 
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser firefox
pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser firefox
pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases --browser firefox
pytest -s -v -m "regression" --html=./Reports/report.html testCases --browser firefox

2. Running the Batch File located in this directory:
   Test can also be executed by running the batch file located in this directory.
   Double click on in or switch directory to this directory on command prompt and run the batch file from there
   N/B: The batch file will run on default browser for now, but can be edited .
   



