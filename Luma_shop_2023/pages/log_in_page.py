from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.my_account_page import MyAccountPage


class LogInPage(BasePage):
    email_field = (By.ID, "email")
    password_field = (By.ID, "pass")
    log_in_button = (By.ID, "send2")
    sign_in_button_from_homepage = (By.LINK_TEXT, "Sign In")
    arrow_to_account = (By.CSS_SELECTOR, "body > div.page-wrapper > header > div.panel.wrapper > div > ul > li.customer-welcome > span > button")
    my_account_button =(By.LINK_TEXT,"My Account")

    def __init__(self, driver):
        super().__init__(driver)

    def click_sign_in_button(self):
        self.click(self.sign_in_button_from_homepage)

    def set_log_in_email(self, log_in_email):
        self.set(self.email_field, log_in_email)

    def set_log_in_password(self, log_in_password):
        self.set(self.password_field, log_in_password)

    def click_log_in_button(self):
        self.click(self.log_in_button)
        return MyAccountPage(self.driver)

    def go_back_to_your_account(self):
        self.click(self.arrow_to_account)
        self.click(self.my_account_button)

