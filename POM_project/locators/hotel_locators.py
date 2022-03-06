class SearchHotelLocators:
    search_hotel_search_xpath = '//*[@id="s2id_autogen8"]/a'
    search_hotel_input_xpath = '//*[@id="select2-drop"]/div/input'
    location_match = '//span[text()="Dubai"]'
    check_in_input_name = 'checkin'
    check_out_input_name = 'checkout'
    travellers_input_id = 'travellersInput'
    adult_input_id = 'adultInput'
    child_input_id = 'childInput'
    search_button_xpath = '//button[text()=" Search"]'


class SearchResultsLocators:
    hotel_names_list_xpath = '//h4[contains(@class,"list_title")]//b'
    hotel_prices_xpath = '//div[contains(@class,"price_tab")]//b'
