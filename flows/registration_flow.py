from pages import create_an_account_page
from pages.create_an_account_page import CreateAnAccountPage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage


class RegistrationFlow:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.create_an_account_page = CreateAnAccountPage(driver)
        self.my_account_page = MyAccountPage(driver)

    def start_registration(self, email: str):
        self.login_page.open()
        self.login_page.type_new_account_email(email)
        self.login_page.click_create_account_btn()
        self.create_an_account_page.wait_for_h1()

    def complete_registration(self, gender, first_name, last_name, password, day, month, year):
        self.create_an_account_page.choose_gender(gender)
        self.create_an_account_page.fill_personal_info(first_name, last_name, password)
        self.create_an_account_page.set_birth_date(day, month, year)
        self.create_an_account_page.submit()
        self.my_account_page.wait_for_green_banner()

    def registration_with_wrong_password(self, gender, first_name, last_name, password, day, month, year):
        self.create_an_account_page.choose_gender(gender)
        self.create_an_account_page.fill_personal_info(first_name, last_name, password)
        self.create_an_account_page.set_birth_date(day, month, year)
        self.create_an_account_page.submit()
        self.create_an_account_page.wait_for_red_banner()
