from selenium.webdriver.common.by import By
from locators.hotel_locators import SearchResultsLocators


class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.hotel_names_list_xpath = SearchResultsLocators.hotel_names_list_xpath
        self.hotel_prices_xpath = SearchResultsLocators.hotel_prices_xpath

    def get_hotel_names(self):
        hotels = self.driver.find_elements(By.XPATH, SearchResultsLocators.hotel_names_list_xpath)
        return [hotel.get_attribute('textContent') for hotel in hotels]

    def get_hotel_prices(self):
        prices = self.driver.find_elements(By.XPATH, SearchResultsLocators.hotel_prices_xpath)
        return [price.get_attribute('textContent') for price in prices]
