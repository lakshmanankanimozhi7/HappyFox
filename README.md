
#HAPPYFOX

## Python Setup
1. Install python 3.9.x version
2. pip install --user pipenv
3. create python virtual env: virtualenv venv
4. source virtualenv/bin/activate
5. Install the python modules from requirement.txt file

## Set path 
1. Provide path of the webdriver in src/tests/base_test.py

## Automation Framework
1. Framework Directory Structure:

```
src
    pages: Page elements from the web page
    helpers : Reusable helper classes that perform actions on page elements
    tests : Test classes that define test methods for each use cases
```

## How to run tests
```
run tests:  pytest src/tests/web/happy_fox_test.py --self-contained-html --html=report.html

run tests in parallel using marker: pytest -v -m happy_fox_tests -n 4 --self-contained-html --html=report.html

run tests with re-run failed tests: pytest -v --reruns 2 -m happy_fox_tests -n 4 --self-contained-html --html=report.html
        (re-run the failed test twice before marking it as failure)

run individual test: pytest -v src/tests/web/happy_fox_test.py -k test_name

run parallel test with json file : py.test -v --reruns 2 -m happy_fox_tests -n 4 --self-contained-html --html=contractor_web_tests.html --json=contractor_web.json

```
