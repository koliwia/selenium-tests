from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestHomepageLuma:

    @pytest.fixture()
    def setup(self):
        s = Service('C://chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()

    def test_check_homepage(self, setup):
        self.driver.get('https://magento.softwaretestingboard.com/')
        self.driver.maximize_window()


