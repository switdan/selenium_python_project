import pytest

from flows.registration_flow import RegistrationFlow
from test_data.registration_data import RegistrationDataGenerator

class TestPositiveScenarios:

    @pytest.mark.registration
    @pytest.mark.positive
    @pytest.mark.debug
    def test_registration(self, driver):
        flow = RegistrationFlow(driver)
        data = RegistrationDataGenerator()

        flow.start_registration(data.EMAIL)
        assert flow.create_an_account_page.get_h1_title() == "CREATE AN ACCOUNT", "Registration page title didn't match"

        flow.complete_registration(data.GENDER, data.FIRST_NAME, data.LAST_NAME, data.PASSWORD, data.DAY, data.MONTH, data.YEAR)
        assert flow.my_account_page.get_green_banner_text() == "Your account has been created.", "Green banner text didn't match"




