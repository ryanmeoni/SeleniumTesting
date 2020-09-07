from selenium.webdriver.common.by import By

class RegisterPageLocators(object):

    USERNAME_INPUT = (By.ID, "id_username")
    USERNAME_CONFLICT_ERROR_MSG = (By.ID, "error_1_id_username")
    EMAIL_INPUT = (By.ID, "id_email")
    PASSWORD_INPUT_ONE = (By.ID, "id_password1")
    PASSWORD_INPUT_TWO = (By.ID, "id_password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".btn")

