# Flask Testing Project

## Overview

This project demonstrates the implementation of unit tests, integration tests and end-to-end (E2E) tests for a sample Flask application.
It uses **Pytest** for automated testing and **Selenium** for browser-based validation.
A Jenkins pipeline is included to automate test execution in a Continuous Integration (CI) environment.

---

## Project Objectives

* Implement and understand different layers of testing:

  * Unit Testing
  * Integration Testing
  * End-to-End (E2E) Testing
* Use Pytest for test automation.
* Use Selenium WebDriver for browser-based testing.
* Demonstrate Continuous Integration setup using Jenkins.

---

## Folder Structure

```
flask-testing/
├── app.py
├── test_unit.py
├── test_integration.py
├── test_e2e.py
├── requirements.txt
├── Jenkinsfile
├── .gitignore
└── README.md
```

---

## 1. Flask Application

### Description

The Flask application (`app.py`) contains three endpoints:

| Endpoint        | Method | Description                     |
| --------------- | ------ | ------------------------------- |
| `/`             | GET    | Health check endpoint           |
| `/add?a=3&b=5`  | GET    | Adds two numbers                |
| `/greet/<name>` | GET    | Returns a personalized greeting |

### Run Application

```bash
python app.py
```

Access the app at: `http://127.0.0.1:5000/`

---

## 2. Unit Testing

### Description

Unit tests verify individual endpoints and ensure each route performs as expected.
Flask’s built-in test client is used for isolated testing.

### Run Unit Tests

```bash
pytest test_unit.py -v
```

---

## 3. Integration Testing

### Description

Integration tests validate interactions between multiple endpoints.
For example, one test adds two numbers and uses the result in another endpoint.

### Run Integration Tests

```bash
pytest test_integration.py -v
```

---

## 4. End-to-End (E2E) Testing

### Description

E2E tests simulate a real user accessing the running application in a browser using Selenium WebDriver.
This validates that the system works as a whole.

### Run E2E Tests

Before running the E2E test:

1. Start the Flask app in one terminal:

   ```bash
   python app.py
   ```
2. In another terminal, run:

   ```bash
   pytest test_e2e.py -v
   ```

---

## 5. Dependencies

### Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

### Requirements File

```
flask
pytest
selenium
webdriver-manager
```

---

## 6. Continuous Integration (Jenkins Setup)

### Description

A Jenkins pipeline is provided to automate the testing process.
It includes separate stages for:

* Checking out the code
* Setting up Python environment
* Running unit, integration and E2E tests

### Steps to Set Up in Jenkins

1. Create a new Jenkins Pipeline job.
2. Select "Pipeline script from SCM".
3. Add repository URL:

   ```
   https://github.com/Extraordinarytechy/flask-testing.git
   ```
4. Save and run the build.

### Jenkinsfile Summary

* Creates a Python virtual environment.
* Installs dependencies from `requirements.txt`.
* Executes tests in separate stages.
* Generates XML test reports for visualization in Jenkins.

---

## 7. How to Use This Project

1. Clone the repository:

   ```bash
   git clone https://github.com/Extraordinarytechy/flask-testing.git
   cd flask-testing
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run Flask app and tests as described above.

---