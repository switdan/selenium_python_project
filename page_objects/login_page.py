from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class HomePage(BasePage):
    __url = "https://automationpractice.techwithjatin.com/login?back=my-account"
    __create_an_account_btn = (By.XPATH, "//a[@class='login']")
    __create_account_email_address_type_field = (By.ID, "email_create")
    __create_account_btn = (By.ID, "SubmitCreate")
    __new_account_email = "test@test.com"


    def type_new_account_email(self):
        self._type(self.__create_account_email_address_type_field, self.__new_account_email)

    def click_sign_in_btn(self):
        self._click(self.__create_an_account_btn)