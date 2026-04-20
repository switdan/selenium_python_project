from pages.login_page import LoginPage


class LogInFlow:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def log_in(self, email, password):
        self.login_page.open()
        self.login_page.type_existed_email(email)
        self.login_page.type_existed_password(password)
        self.login_page.click_sign_in_btn()