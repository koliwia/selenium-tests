import pytest
from selenium import webdriver
from pages.search_hotel import SearchHotelPage
from selenium.webdriver.chrome.service import Service
from pages.search_hotel_results import SearchResultsPage


class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        s = Service('C://chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()

    def test_hotel_search(self, setup):
        self.driver.get('http://www.kurs-selenium.pl/demo/')
        self.driver.maximize_window()
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city('Dubai')
        search_hotel_page.set_date_range('12/03/2022', '19/03/2022')
        search_hotel_page.set_travellers('2', '2')
        search_hotel_page.perform_search()
        results_page = SearchResultsPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        price_values = results_page.get_hotel_prices()

        assert hotel_names[0] == 'Jumeirah Beach Hotel'
        assert hotel_names[1] == 'Oasis Beach Tower'
        assert hotel_names[2] == 'Rose Rayhaan Rotana'
        assert hotel_names[3] == 'Hyatt Regency Perth'

        assert price_values[0] == '$22'
        assert price_values[1] == '$50'
        assert price_values[2] == '$80'
        assert price_values[3] == '$150'

