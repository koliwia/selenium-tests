from selenium.webdriver.common.by import By

from POM_project.search_hotel_test import driver


class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.hotel_names_list_xpath = '//h4[contains(@class,"list_title")]//b'
        self.hotel_prices_xpath = '//div[contains(@class,"price_tab")]//b'

    def get_hotel_names(self):
        hotels = self.driver.find_elements(By.XPATH, self.hotel_names_list_xpath)
        return [hotel.get_attribute('textContent') for hotel in hotels]

    def get_hotel_prices(self):
        prices = self.driver.find_elements(By.XPATH, '//div[contains(@class,"price_tab")]//b')
        return [price.get_attribute('textContent') for price in prices]
