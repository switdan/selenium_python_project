from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CreateAnAccountPage(BasePage):
    _URL = "https://automationpractice.techwithjatin.com/login?back=my-account#account-creation"

    _H1_TITLE = (By.XPATH, "//h1[text()='Create an account']")
    _TITLE_GENDER_MALE = (By.ID, "id_gender1")
    _TITLE_GENDER_FEMALE = (By.ID, "id_gender2")
    _FIRST_NAME = (By.ID, "customer_firstname")
    _LAST_NAME = (By.ID, "customer_lastname")
    _MAIL = (By.ID, "email")
    _PASSWORD = (By.ID, "passwd")
    _DAYS_OF_BIRTH = (By.ID, "days")
    _MONTH_OF_BIRTH = (By.ID, "months")
    _YEAR_OF_BIRTH = (By.ID, "years")
    _REGISTER_BTN = (By.ID, "submitAccount")
    _RED_BANNER = (By.XPATH, "//div[@class='alert alert-danger']")
    _RED_BANNER_2ND_LINE = (By.XPATH, "//div[@class='alert alert-danger']/p")


    def open(self):
        self._open_url(self._URL)

    def h1_title(self) -> str:
        return self.get_text(self._H1_TITLE)

    def get_registration_url(self) -> str:
        return self._URL

    def choose_gender(self, gender: str):
        if gender == "M":
            self._click(self._TITLE_GENDER_MALE)
        elif gender == "F":
            self._click(self._TITLE_GENDER_FEMALE)
        else:
            raise ValueError("Invalid gender")

    def fill_personal_info(self, first_name, last_name, password):
        self._type(self._FIRST_NAME, first_name)
        self._type(self._LAST_NAME, last_name)
        self._type(self._PASSWORD, password)

    def set_birth_date(self, day, month, year):
        self._select(self._DAYS_OF_BIRTH, day)
        self._select(self._MONTH_OF_BIRTH, month)
        self._select(self._YEAR_OF_BIRTH, year)

    def submit(self):
        self._click(self._REGISTER_BTN)

    def wait_for_h1(self):
        self.wait_for_loaded(self._H1_TITLE)

    def red_banner_wrong_pswd(self) -> str:
        return self.get_text(self._RED_BANNER)


    def wait_for_red_banner(self):
        self.wait_for_loaded(self._RED_BANNER)