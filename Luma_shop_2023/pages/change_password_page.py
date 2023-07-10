from pages.base_page import BasePage
from utilities.locators import ChangePasswordFields


class ChangePasswordPage(BasePage):

    def __init__(self, driver):
        self.locators = ChangePasswordFields
        super().__init__(driver)

    def change_password(self, first_name, last_name, current_password, new_password, confirm_new_password):
        self.click(self.locators.change_password_button)
        self.set(self.locators.first_name_field, first_name)
        self.set(self.locators.last_name_field, last_name)
        self.set(self.locators.current_password_field, current_password)
        self.set(self.locators.new_password_field, new_password)
        self.set(self.locators.confirm_new_password_field, confirm_new_password)
        self.click(self.locators.save_button)

