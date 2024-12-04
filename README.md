# Python tests for web app.

This project is a web application with automated tests implemented in Python using `pytest` and `selenium`. This README provides guidelines to set up the environment, run the tests, and configure the necessary environment variables.

---

## **Requirements**
Ensure your machine meets the following requirements:
- **Python**: Version 3.8 or higher.
- **pip**: Python package manager.
- **Chrome**: Google Chrome browser installed.
- **Git**: To clone the repository.
- **Virtual environment**: It is recommended to use a virtual environment (`venv`).

---

## **Environment Setup**

1. **Clone the repository**

```bash
   git clone https://github.com/YOUR_USERNAME/test-py-web-app.git
   cd test-py-web-app
```

### Windows 

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux

```bash	
 python3 -m venv .venv
source .venv/bin/activate
```	

# Install the dependencies

```bash
pip install -r requirements.txt
```
## **Environment Variables Setup**
Ensure the following variables are correctly configured on your machine:

* PATH: Include the path to the Python executable and pip. For example:

   * Windows: C:\Python3x and C:\Python3x\Scripts
   
   * Linux/Mac: /usr/bin/python3 and /usr/local/bin

* ChromeDriver: You don’t need to manually download ChromeDriver because webdriver-manager handles it automatically. However, ensure Google Chrome is installed and updated.

## **Running the Tests**

* Unit Tests to run the unit tests:

```bash
pytest src/tests/test_unit.py -v -s
```

* API Tests to run the API tests:

```bash
pytest src/tests/test_api.py -v -s
```

* End-to-End(E2E) Tests to run the E2E tests:

```bash
pytest src/tests/test_e2e.py -v -s
```

## **Troubleshooting**

* Error resolving modules (Import could not be resolved)

   * Ensure the virtual environment is activated and dependencies are correctly installed.
   * Reinstall the dependencies:
```bash
pip install -r requirements.txt
```

* ChromeDriver Error

   * Verify that the Google Chrome browser is installed and up-to-date.
   * Clear the webdriver-manager cache:

```bash
rm -rf ~/.wdm
```

*Error activating the virtual environment

   * Ensure you are using the correct terminal (bash, cmd, or PowerShell).
   * Use the appropriate commands for your operating system (see "Environment Setup" section).

## **Contribution**

Contributions are welcome! Feel free to open issues and submit pull requests.

## **License**

This project is licensed under the [MIT license](https://opensource.org/license/mit)

