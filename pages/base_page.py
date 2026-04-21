import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(EC.visibility_of_element_located(locator))

    def _open_url(self, url: str):
        self._driver.get(url)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _select(self, locator: tuple, value, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        Select(self._find(locator)).select_by_value(str(value))


    def get_text (self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def wait_for_loaded(self, locator: tuple, time: int = 10):
        WebDriverWait(self._driver, time).until(
            EC.visibility_of_element_located(locator)
        )

    def _hover(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        ActionChains(self._driver).move_to_element(self._find(locator)).perform()

    def _switch_to_iframe(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._driver.switch_to.frame(self._find(locator))

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def wait_for_page(self, text: str, time: int = 10) -> bool:
        WebDriverWait(self._driver, time).until(EC.url_contains(text))
        return text in self._driver.current_url

    def _find_all(self, locator: tuple) -> list:
        return self._driver.find_elements(*locator)

    def _get_random_product(self):
        """
        Finds all unique products on the page and returns a randomly selected one.
        Deduplicates products by href to avoid selecting the same product from multiple sections.

        :return: Tuple of (product_name, product_price, product_url)
        """
        products = (By.XPATH, "//li//div[@class='product-container']")
        products = self._find_all(products)
        seen = set()
        unique_products = []

        for p in products:
            href = p.find_element(By.CLASS_NAME, "product_img_link").get_attribute("href")
            if href not in seen:
                seen.add(href)
                unique_products.append(href)

        product_url = random.choice(unique_products)
        product = (By.XPATH,
                   f"(//a[@class='product-name' and @href='{product_url}']/ancestor::div[@class='product-container'])[1]")
        product_text = self._find(product).text
        parts = product_text.split("\n")
        product_name = parts[0].strip()
        product_price = parts[1].split()[0].strip()

        return product_name, product_price, product_url