from pages.sign_up_page import SignUpPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestSignUp(BaseTest):

    def test_valid_registration_data(self):
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

    def test_invalid_registration_data(self):
        signup_page = SignUpPage(self.driver)
        signup_page.create_an_account(
            "","","invalidemail.com","abc","asd")
        signup_page.signup_button()
        error_firstname = "This is a required field."
        error_lastname = "This is a required field."
        error_email = "Please enter a valid email address (Ex: johndoe@domain.com)."
        error_password_min_length = "Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored."
        error_confirm_password_not_equal = "Please enter the same value again."

        assert [error_firstname,error_lastname,error_email,error_password_min_length,error_confirm_password_not_equal] == signup_page.get_error_messages()