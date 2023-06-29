from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

s = Service('C://chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://www.kurs-selenium.pl/demo/')
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="s2id_autogen8"]/a').click()
driver.find_element(By.XPATH, '//*[@id="select2-drop"]/div/input').send_keys('Dubai')
wait = WebDriverWait(driver, 2)
wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Dubai"]'))).click()
driver.find_element(By.NAME, 'checkin').click()
driver.find_element(By.XPATH, '//td[@class="day " and text()="30"]').click()
elements = driver.find_elements(By.XPATH, '//td[@class="day " and text()="19"]')
for e in elements:
    if e.is_displayed():
        e.click()
        break

driver.find_element(By.ID, 'travellersInput').click()
driver.find_element(By.ID, 'adultInput').clear()
driver.find_element(By.ID, 'adultInput').send_keys('2')
driver.find_element(By.ID, 'childInput').clear()
driver.find_element(By.ID, 'childInput').send_keys('1')
driver.find_element(By.XPATH, '//button[text()=" Search"]').click()

hotels = driver.find_elements(By.XPATH, '//h4[contains(@class,"list_title")]//b')
hotel_names = [hotel.get_attribute('textContent') for hotel in hotels]
for hotel in hotel_names:
    print('The hotel name: ' + hotel)

assert hotel_names[0] == 'Jumeirah Beach Hotel'
assert hotel_names[1] == 'Oasis Beach Tower'
assert hotel_names[2] == 'Rose Rayhaan Rotana'
assert hotel_names[3] == 'Hyatt Regency Perth'

prices = driver.find_elements(By.XPATH, '//div[contains(@class,"price_tab")]//b')
price_values = [price.get_attribute('textContent') for price in prices]
for price in price_values:
    print('The price is: ' + price)


assert price_values[0] == '$22'
assert price_values[1] == '$50'
assert price_values[2] == '$80'
assert price_values[3] == '$150'

driver.quit()