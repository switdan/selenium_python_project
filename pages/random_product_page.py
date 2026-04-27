from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RandomProductPage(BasePage):
    _URL = None
    _PRODUCT_PRICE_LOCATOR = (By.ID, "our_price_display")
    _PRODUCT_NAME_LOCATOR = (By.XPATH, "//h1[@itemprop='name']")
    _ADD_TO_CART_BTN = (By.ID, "add_to_cart")

    def product_price(self) -> str:
        return self.get_text(self._PRODUCT_PRICE_LOCATOR)

    def product_name(self) -> str:
        return self.get_text(self._PRODUCT_NAME_LOCATOR)

    def click_add_to_cart(self):
        self._click(self._ADD_TO_CART_BTN)