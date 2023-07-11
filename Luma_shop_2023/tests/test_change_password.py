from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import change_password_page
from pages.change_password_page import ChangePasswordPage
from pages.log_in_page import LogInPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestChangePassword(BaseTest):
    def test_change_password_failure(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.click_sign_in_button()
        log_in_page.set_log_in_email(TestData.log_in_email)
        log_in_page.set_log_in_password(TestData.log_in_password)
        log_in_page.click_log_in_button()

        # Wait for welcome message to appear
        wait_time = 10
        try:
            WebDriverWait(log_in_page.driver, wait_time).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                                                                 "body > div.page-wrapper > header > div.panel.wrapper > div > ul > li.greet.welcome > span"),
                                                                                                'Welcome, dsfdsf sdfsdfsd!'))
            print("Customer logged in")
        except TimeoutException:
            print("Loading took too much time")

        log_in_page.go_back_to_your_account()

        change_password_page = ChangePasswordPage(self.driver)
        change_password_page.change_password("dsfdsf", "sdfsdfsd", "test123!", "test1234!", "test234!")

        # Wait for confirm password incorrect validation message
        try:
            WebDriverWait(log_in_page.driver, wait_time).until(
                EC.text_to_be_present_in_element((By.ID, "password-confirmation-error"),
                                                 'Please enter the same value again.'))
            print("Validation message displayed")
        except TimeoutException:
            print("Loading took too much time")

        # Check if checkbox is selected
        checkbox = change_password_page.find_and_check_if_selected()
        assert checkbox.is_selected()
