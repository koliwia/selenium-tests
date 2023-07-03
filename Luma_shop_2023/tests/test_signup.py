from pages.sign_up_page import SignUpPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestSignUp(BaseTest):

    def test_valid_credentials(self):
        signup_page = SignUpPage(self.driver)
        signup_page.set_first_name(TestData.first_name)
        signup_page.set_last_name(TestData.last_name)
        signup_page.click_newsletter_tickbox()
        signup_page.set_email_address(TestData.email_address)
        signup_page.set_password(TestData.password)
        signup_page.set_confirm_password(TestData.confirm_password)
        signup_page.signup_button()

        title_after_registration = signup_page.get_title()
        assert title_after_registration == "My Account"
