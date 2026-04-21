import random

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class HomePage(BasePage):
    _URL = "https://automationpractice.techwithjatin.com/"

    _SIGN_IN_BTN = (By.XPATH, "//a[@class='login']")

    def open(self):
        self._open_url(self._URL)

    def click_sign_in(self):
        self._click(self._SIGN_IN_BTN)

    def get_random_product_from_home_page(self):
        return self._get_random_product()

    def click_product_quick_view(self, product_url):
        product_img = (By.XPATH, f"//a[@class='product_img_link' and @href='{product_url}']")
        self._hover(product_img)

        quick_view_btn = (By.XPATH, f"//a[@class='quick-view' and @rel='{product_url}']")
        self._click(quick_view_btn)