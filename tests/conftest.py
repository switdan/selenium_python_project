import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

REPORT_PATH = "reports/report.html"

@pytest.fixture()
def driver(request):
    """
    Pytest fixture that initializes a Selenium WebDriver based on the --browser option.
    Yields the driver instance and ensures quit() is called after test execution.

    :param request: Pytest fixture request object used to access CLI options
    :return: Selenium WebDriver instance
    """
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver...")
    if browser == "chrome":
        options = Options()
        options.add_argument("--window-size=1920,1080")
        my_driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
        my_driver.set_window_size(1920, 1080)

    else:
        raise Exception(f"Invalid browser. Expected 'chrome' or 'firefox', but got {browser}")
    yield my_driver
    print(f"Closing {browser} driver.")
    my_driver.quit()

def pytest_addoption(parser):
    """
    Pytest hook that registers the --browser CLI option to select the target browser.

    :param parser: Pytest parser object used to register command-line options
    """
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome, firefox)")
