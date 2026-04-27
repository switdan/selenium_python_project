## Installation
Clone the repository (the first time) using HTTPS:
```bash
git clone https://github.com/switdan/seleniu_python_project.git
```
or using SSH
```bash
git clone git@github.com:switdan/seleniu_python_project.git
```
Create a virtual environment in the project directory and activate it (if you already have one, skip to step 3):


Install / update the required libraries – you can do this using Sync in PyCharm or directly in the terminal:
```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests (HTML report is generated automatically to `reports/report.html`):
```bash
pytest
```

Run tests by marker:
```bash
pytest -m registration   # All registration tests
pytest -m login          # All login tests
pytest -m positive       # All positive path tests
pytest -m negative       # All negative path tests
pytest -m products       # All product page tests
pytest -m purchase       # All tests with purchase
pytest -m debug          # Single test debug mode (no extra reports)
```

Run tests on a specific browser (default: chrome):
```bash
pytest --browser chrome
pytest --browser firefox
```

Open HTML report automatically after test session:
```bash
pytest --open-report
```

## Project Structure
```
seleniu_python_project/
├── flows/          # Multi-page test flows
├── pages/          # Page Object Model classes
├── test_data/      # Test data generators and expected messages
├── tests/          # Test files and conftest.py
├── reports/        # Auto-generated HTML test reports
└── pytest.ini      # Pytest configuration and markers
```