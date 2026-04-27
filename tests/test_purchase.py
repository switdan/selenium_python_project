import time

import pytest

from flows.log_in_flow import LogInFlow
from flows.purchase_flow import PurchaseFlow
from pages.order_page import Order
from test_data.registration_data import get_login_data


class TestPurchase:
    @pytest.mark.products
    @pytest.mark.positive
    @pytest.mark.purchase
    @pytest.mark.debug
    @pytest.mark.parametrize("email, password, fullname",
                             get_login_data("test_data/logged_user.csv"))
    def test_purchase(self, driver, email, password, fullname):
        log_in = LogInFlow(driver)
        flow = PurchaseFlow(driver)
        order = Order(driver)

        log_in.log_in(email, password)

        flow.choose_product_from_main_page_and_add_to_cart()
        flow.go_to_order_page()
        assert flow.product_name == order.product_name(), "Product name is not the same on the main page and product page"
        assert flow.product_price == order.product_price(), "Product price is not the same on the main page and product page"

        flow.go_to_order_page_and_move_to_payment()
        assert order.payment_title_text_shown() == order.payment_title_text_expected()


