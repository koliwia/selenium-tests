from selenium.webdriver.common.by import By


class ChangePasswordFields:
    change_password_button = (By.LINK_TEXT, "Change Password")
    first_name_field = (By.ID, "firstname")
    last_name_field = (By.ID, "lastname")
    change_password_checkbox = (By.ID, "change-password")
    current_password_field = (By.ID, "current-password")
    new_password_field = (By.ID, "password")
    confirm_new_password_field = (By.ID, "password-confirmation")
    save_button = (By.CSS_SELECTOR, "#form-validate > div > div.primary > button")
    confirm_password_validation_message = (By.ID, "password-confirmation-error")