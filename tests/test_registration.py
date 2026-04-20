import pytest

from flows.registration_flow import RegistrationFlow

class TestPositiveScenarios:

    @pytest.mark.registration
    @pytest.mark.positive
    @pytest.mark.debug
    @pytest.mark.parametrize(
        "mail, expected_header, gender, first_name, last_name, password, day, month, year, expected_banner_msg",
        [("test16yh2ddafqs8dss3@test.com", "CREATE AN ACCOUNT", "M", "Daniel", "Świtała", "ZSHJFHALHJ123!", "12", "10", "1990", "Your account has been created.")]
    )
    def test_registration(self, driver, mail, expected_header, gender, first_name, last_name, password, day, month, year, expected_banner_msg):
        flow = RegistrationFlow(driver)

        flow.start_registration(mail)
        assert flow.create_an_account_page.get_h1_title() == expected_header, "Registration page title didn't match"

        flow.complete_registration(gender, first_name, last_name, password, day, month, year, expected_banner_msg)
        assert flow.my_account_page.get_green_banner_text() == expected_banner_msg, "Green banner text didn't match"




