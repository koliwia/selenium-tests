from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

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

        title_after_log_in = log_in_page.get_title()
        assert title_after_log_in == "Home Page"

    def test_log_in_with_invalid_credentials(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.click_sign_in_button()
        log_in_page.set_log_in_email(TestData.invalid_log_in_email)
        log_in_page.set_log_in_password(TestData.invalid_log_in_password)
        log_in_page.click_log_in_button()
        WebDriverWait(driver, 2)
        title_after_invalid_log_in = log_in_page.get_title()
        assert title_after_invalid_log_in == "Customer Login"
        assert 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.' in log_in_page.driver.page_source



