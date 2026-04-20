import pytest

from flows.registration_flow import RegistrationFlow
from test_data.registration_data import RegistrationDataGenerator, get_emails_from_csv
from test_data.expected_messages import ExpectedMessages

class TestPositiveScenarios:

    @pytest.mark.registration
    @pytest.mark.positive
    def test_registration(self, driver):
        data = RegistrationDataGenerator()
        flow = RegistrationFlow(driver)

        flow.start_registration(data.email)
        assert flow.create_an_account_page.h1_title() == ExpectedMessages.REGISTRATION_HEADER, "Registration page title didn't match"

        flow.complete_registration(data.gender, data.first_name, data.last_name, data.password, data.day, data.month, data.year)
        assert flow.my_account_page.green_banner_text() == ExpectedMessages.REGISTRATION_BANNER, "Green banner text didn't match"

class TestNegativeScenarios:

    @pytest.mark.registration
    @pytest.mark.negative
    @pytest.mark.debug
    @pytest.mark.parametrize(
        "email, expected_message",
        [("", ExpectedMessages.INVALID_EMAIL_ADDRESS)] +
        [(email, ExpectedMessages.EMAIL_REGISTERED_ALREADY)
         for email in get_emails_from_csv("test_data/registration.csv")])
    def test_registration_wrong_email(self, driver, email, expected_message):
        flow = RegistrationFlow(driver)

        flow.start_registration_with_specific_email(email)
        assert flow.login_page.red_banner_text() == expected_message, "Red banner text didn't match"


    @pytest.mark.registration
    @pytest.mark.negative
    def test_registration_wrong_password(self, driver):
        data = RegistrationDataGenerator()
        flow = RegistrationFlow(driver)

        flow.start_registration(data.email)
        flow.registration_with_wrong_password(data.gender, data.first_name, data.last_name, data.password_max_4, data.day, data.month, data.year)
        assert flow.create_an_account_page.red_banner_wrong_pswd() == ExpectedMessages.PASSWORD_IS_INVALID, "Red banner text didn't match"



