from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class HomePage(BasePage):
    __url = "https://automationpractice.techwithjatin.com/"
    __sign_in_btn = (By.XPATH, "//a[@class='login']")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def click_sign_in(self):
        self._click(self.__sign_in_btn)