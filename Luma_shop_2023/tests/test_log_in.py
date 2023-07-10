from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        log_in_page.set_log_in_email(TestData.email_address)
        log_in_page.set_log_in_password(TestData.password)
        log_in_page.click_log_in_button()
        title_after_invalid_log_in = log_in_page.get_title()
        assert title_after_invalid_log_in == "Customer Login"
        wait_time = 10
        try:
            WebDriverWait(log_in_page.driver, wait_time).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#maincontent > div.page.messages > div:nth-child(2) > div > div > div"),'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'))
            print
            "Succeeded"
        except TimeoutException:
            print
            "Loading took too much time"


