# Test Automation Sample Project

This sample project demonstrates how to automate tests for a simple web application using Playwright and Python.

## UI Automated Tests
The UI tests are written in Python using the Playwright library. The target application is the login page at [The Internet](https://the-internet.herokuapp.com/login), showcasing simple login and secure area page validations.

### Running the Tests Locally
From the root of the project, run the following command to build the Docker image and run the tests inside the container:  
_NOTE: Make sure you have Docker installed on your machine._
```sh
make all
```
### To build the Docker image only, run:
```sh
make build
```
### To run the tests inside the container, use:
* For all browsers:
```sh
make run-all-tests
```
* For Chrome:
```sh
make run-all-chromium-tests
```
* For Firefox:
```sh
make run-all-firefox-tests
```

