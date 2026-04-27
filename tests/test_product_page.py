import pytest

from flows.products_flow import ProductsFlow
from pages.random_product_page import RandomProductPage
from pages.random_product_quick_view import RandomProductQuickView


class TestProductPage:

    @pytest.mark.products
    @pytest.mark.positive
    def test_product_compare_home_page_product_page(self, driver):
        flow = ProductsFlow(driver)
        product_page = RandomProductPage(driver)

        flow.choose_product_from_main_page()
        flow.open_chosen_product_page()
        assert flow.product_name == product_page.product_name(), "Product name is not the same on the main page and product page"
        assert flow.product_price == product_page.product_price(), "Product price is not the same on the main page and product page"

    @pytest.mark.products
    @pytest.mark.positive
    def test_product_compare_home_page_quick_view(self, driver):
        flow = ProductsFlow(driver)
        product_quic_view = RandomProductQuickView(driver)

        flow.choose_product_from_main_page()
        flow.open_chosen_product_quick_view()
        product_quic_view.switch_to_quick_view()
        assert flow.product_name == product_quic_view.product_name(), "Product name is not the same on the main page and product page"
        assert flow.product_price == product_quic_view.product_price(), "Product price is not the same on the main page and product page"

