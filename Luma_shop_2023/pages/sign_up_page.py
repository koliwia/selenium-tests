from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.my_account_page import MyAccountPage


class SignUpPage(BasePage):
    first_name_field = (By.ID, "firstname")
    last_name_field = (By.ID, "lastname")
    signup_tickbox = (By.ID, "is_subscribed")
    email_field = (By.ID, "email_address")
    password_field = (By.ID, "password")
    confirm_password_field = (By.ID, "password-confirmation")
    create_account_button = (By.XPATH, "//div[@class='actions-toolbar']//button[@title='Create an Account']")
    firstname_validation_message = (By.ID, "firstname-error")
    lastname_validation_message = (By.ID, "lastname-error")
    email_validation_message = (By.ID, "email_address-error")
    password_validation_message = (By.ID, "password-error")
    password_confirmation_validation_message = (By.ID, "password-confirmation-error")
    create_an_account_button_from_homepage = (By.LINK_TEXT, "Create an Account")

    def __init__(self, driver):
        super().__init__(driver)

    def click_signup_page(self):
        self.click(self.create_an_account_button_from_homepage)

    def set_first_name(self, first_name):
        self.set(self.first_name_field, first_name)

    def set_last_name(self, last_name):
        self.set(self.last_name_field, last_name)

    def click_newsletter_tickbox(self):
        self.click(self.signup_tickbox)

    def set_email_address(self, email_address):
        self.set(self.email_field, email_address)

    def set_password(self, password):
        self.set(self.password_field, password)

    def set_confirm_password(self, confirm_password):
        self.set(self.confirm_password_field, confirm_password)

    def signup_button(self):
        self.click(self.create_account_button)
        return MyAccountPage(self.driver)

    def create_an_account(self, first_name, last_name, email_address, password, confirm_password):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.click_newsletter_tickbox()
        self.set_email_address(email_address)
        self.set_password(password)
        self.set_confirm_password(confirm_password)

    def get_error_messages(self):
        return [self.get_text(self.firstname_validation_message),
                self.get_text(self.lastname_validation_message),
                self.get_text(self.email_validation_message),
                self.get_text(self.password_validation_message),
                self.get_text(self.password_confirmation_validation_message)]
