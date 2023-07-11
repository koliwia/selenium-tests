from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def set(self, locator, value):
        self.find(locator).clear()
        self.find(locator).send_keys(value)

    def get_text(self, locator):
        return self.find(locator).text

    def get_title(self):
        return self.driver.title

    def click_top_page_menu(self, page_name):
        page = By.XPATH, "//ul[@id ='ui-id-2']//span[text()='" + page_name + "']"
        self.click(page)

