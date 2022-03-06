from selenium.webdriver.common.by import By


class SearchHotelPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_hotel_search_xpath = '//*[@id="s2id_autogen8"]/a'
        self.search_hotel_input_xpath = '//*[@id="select2-drop"]/div/input'
        self.location_match = '//span[text()="Dubai"]'
        self.check_in_input_name = 'checkin'
        self.check_out_input_name = 'checkout'
        self.travellers_input_id = 'travellersInput'
        self.adult_input_id = 'adultInput'
        self.child_input_id = 'childInput'
        self.search_button_xpath = '//button[text()=" Search"]'

    def set_city(self, city):
        self.driver.find_element(By.XPATH, self.search_hotel_search_xpath).click()
        self.driver.find_element(By.XPATH, self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element(By.XPATH, self.location_match).click()

    def set_date_range(self, check_in, check_out):
        self.driver.find_element(By.NAME, self.check_in_input_name).send_keys(check_in)
        self.driver.find_element(By.NAME, self.check_out_input_name).send_keys(check_out)

    def set_travellers(self, adults, child):
        self.driver.find_element(By.ID, self.travellers_input_id).click()
        self.driver.find_element(By.ID, self.adult_input_id).clear()
        self.driver.find_element(By.ID, self.adult_input_id).send_keys(adults)
        self.driver.find_element(By.ID, self.child_input_id).clear()
        self.driver.find_element(By.ID, self.child_input_id).send_keys(child)

    def perform_search(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
