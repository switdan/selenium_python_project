import pytest

from flows.log_in_flow import LogInFlow
from pages.my_account_page import MyAccountPage
from test_data.expected_messages import ExpectedMessages
from test_data.registration_data import get_login_data, get_emails_password_from_csv


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    @pytest.mark.parametrize("email, password, fullname",
        get_login_data("test_data/logged_user.csv"))
    def test_log_in_successfully(self, driver, email, password, fullname):
        flow = LogInFlow(driver)
        flow.log_in(email, password)

        flow = MyAccountPage(driver)
        flow.wait_for_my_account_page()

        assert flow.customer_account_full_name() == fullname

class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.debug
    @pytest.mark.parametrize(
        "email, password, expected_message",
        [
            ("", "12345!", ExpectedMessages.MISSING_EMAIL_ADDRESS),
            ("testautomation12@test.pl", "", ExpectedMessages.MISSING_PASSWORD),
            ("testautomation12@test.pl", "wrong_password", ExpectedMessages.AUTHENTICATION_FAILED),
        ]
    )
    def test_log_in_incorrect_values(self, driver, email, password, expected_message):
        flow = LogInFlow(driver)
        flow.log_in(email, password)

        assert flow.login_page.red_banner_text() == expected_message