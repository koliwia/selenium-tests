from pages.log_in_page import LogInPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestLogin(BaseTest):

    def test_log_in_with_valid_credentials(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.click_sign_in_button()
        log_in_page.set_log_in_email(TestData.log_in_email)
        log_in_page.set_log_in_password(TestData.log_in_password)
        log_in_page.click_log_in_button()

        title_after_registration = log_in_page.get_title()
        assert title_after_registration == "Home Page"