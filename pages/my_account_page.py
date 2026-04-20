from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MyAccountPage(BasePage):
    _URL = "https://automationpractice.techwithjatin.com/my-account"

    _GREEN_BANNER = (By.XPATH, "//p[@class='alert alert-success']")

    def get_green_banner_text(self) -> str:
        return self.get_text(self._GREEN_BANNER)

    def wait_for_green_banner(self):
        self.wait_for_loaded(self._GREEN_BANNER)