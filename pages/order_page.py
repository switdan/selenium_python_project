from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Order(BasePage):
    _URL = "https://automationpractice.techwithjatin.com/order"
    _PROCEED_TO_CHECKOUT_BTN_SUMMARY_SECTION = (By.XPATH, '//a[@href="https://automationpractice.techwithjatin.com/order?step=1"]')
    _PROCEED_TO_CHECKOUT_BTN_ADDRESS_SECTION = (By.XPATH, "//button[@class='button btn btn-default button-medium']")
    _PROCEED_TO_CHECKOUT_BTN_SHIPPING_SECTION = (By.XPATH, "//button[@class='button btn btn-default standard-checkout button-medium']")
    _PRODUCT_PRICE_LOCATOR = (By.XPATH, "//ul[@class='price text-right']")
    _PRODUCT_NAME_LOCATOR = (By.XPATH, "(//p[@class='product-name'])[2]")
    _THERMS_OF_SERVICE_LABEL = (By.CSS_SELECTOR, "label[for='cgv']")
    _PAYMENT_TITLE_LOCATOR = (By.XPATH, "//h1[@class='page-heading']")
    _PAYMENT_TITLE_EXPECTED = "PLEASE CHOOSE YOUR PAYMENT METHOD"

    def open(self):
        self._open_url(self._URL)

    def click_proceed_to_checkout_in_summary_section(self):
        self._click(self._PROCEED_TO_CHECKOUT_BTN_SUMMARY_SECTION)

    def click_proceed_to_checkout_in_address_section(self):
        self._click(self._PROCEED_TO_CHECKOUT_BTN_ADDRESS_SECTION)

    def click_proceed_to_checkout_in_shipping_section(self):
        self._click(self._PROCEED_TO_CHECKOUT_BTN_SHIPPING_SECTION)

    def product_price(self) -> str:
        return self.get_text(self._PRODUCT_PRICE_LOCATOR)

    def product_name(self) -> str:
        return self.get_text(self._PRODUCT_NAME_LOCATOR)

    def click_therms_of_service(self):
        self._click(self._THERMS_OF_SERVICE_LABEL)

    def payment_title_text_shown(self) -> str:
        return self.get_text(self._PAYMENT_TITLE_LOCATOR).split('\n')[0]

    def payment_title_text_expected(self) -> str:
        return self._PAYMENT_TITLE_EXPECTED