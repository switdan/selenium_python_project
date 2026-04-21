from pages.home_page import HomePage

class ProductsFlow:
    def __init__(self, driver):
        self.home_page = HomePage(driver)
        self.product_name = None
        self.product_price = None
        self.product_url = None

    def choose_product_from_main_page(self):
        self.home_page.open()
        self.product_name, self.product_price, self.product_url = self.home_page.get_random_product_from_home_page()

    def open_chosen_product_page(self):
        self.home_page._open_url(self.product_url)

    def open_chosen_product_quick_view(self):
        self.home_page.open()
        self.home_page.click_product_quick_view(self.product_url)
