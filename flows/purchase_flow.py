import time

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.order_page import Order
from pages.random_product_page import RandomProductPage

class PurchaseFlow:
    def __init__(self, driver):
        self.home_page = HomePage(driver)
        self.product_page = RandomProductPage(driver)
        self.order_page = Order(driver)
        self.product_name = None
        self.product_price = None
        self.product_url = None

    def choose_product_from_main_page_and_add_to_cart(self):
        self.home_page.open()
        self.product_name, self.product_price, self.product_url = self.home_page.get_random_product_from_home_page()
        self.home_page._open_url(self.product_url)
        self.product_page.click_add_to_cart()
        time.sleep(1) #It'll need to wait a moment here, because if you proceed too quickly, the item may not appear in your cart.

    def go_to_order_page(self):
        self.order_page.open()

    def go_to_order_page_and_move_to_payment(self):
        self.order_page.open()
        self.order_page.click_proceed_to_checkout_in_summary_section()
        self.order_page.click_proceed_to_checkout_in_address_section()
        self.order_page.click_therms_of_service()
        self.order_page.click_proceed_to_checkout_in_shipping_section()


