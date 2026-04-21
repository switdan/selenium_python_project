from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RandomProductQuickView(BasePage):
    _URL = None
    _IFRAME = (By.XPATH, "//iframe[contains(@id,'fancybox-frame')]")
    _PRODUCT_PRICE_LOCATOR = (By.ID, "our_price_display")
    _PRODUCT_NAME_LOCATOR = (By.XPATH, "//h1[@itemprop='name']")

    def switch_to_quick_view(self):
        self._switch_to_iframe(self._IFRAME)

    def product_price(self) -> str:
        return self.get_text(self._PRODUCT_PRICE_LOCATOR)

    def product_name(self) -> str:
        return self.get_text(self._PRODUCT_NAME_LOCATOR)

