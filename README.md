# Test Assessment

A UI automation testing project built with **Python**, **Pytest**, and **Selenium WebDriver**. The framework follows the **Page Object Model (POM)** design pattern to keep the test code organized, reusable, and easy to maintain.

## Technologies Used

* Python 3.10+
* Pytest
* Selenium WebDriver
* WebDriver Manager

## Clone the Repository

```bash
git clone https://github.com/mohamedtaalat/TestAssessment.git
cd TestAssessment
```

## Create a Virtual Environment (Recommended)

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt
```

## Run the Tests

Run all tests:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_wallet.py
```

Run a specific test:

```bash
pytest tests/test_wallet.py::test_wallet_creation
```

## Project Structure

```
TestAssessment/
│
├── pages/
├── tests/
├── conftest.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Author

**Mohamed Talaat**

GitHub: https://github.com/mohamedtaalat
