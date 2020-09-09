from selenium.webdriver.common.by import By

class HomePageLocators(object):

    LOGIN_BUTTON = (By.LINK_TEXT, "Login")
    REGISTER_BUTTON = (By.LINK_TEXT, "Register")
    YOUR_PROFILE_BUTTON = (By.LINK_TEXT, "Your Profile")


class RegisterPageLocators(object):

    # Register input locators
    USERNAME_INPUT = (By.ID, "id_username")
    EMAIL_INPUT = (By.ID, "id_email")
    PASSWORD_INPUT_ONE = (By.ID, "id_password1")
    PASSWORD_INPUT_TWO = (By.ID, "id_password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".btn")

    # Error message locators
    ERROR_USERNAME_CONFLICT_MSG = (By.ID, "error_1_id_username")
    ERROR_PASSWORDS_NO_MATCH_MSG = (By.ID, "error_1_id_password2")


class LoginPageLocators(object):

    # Login input locators
    USERNAME_INPUT = (By.ID, "id_username")
    PASSWORD_INPUT = (By.ID, "id_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn")

    # Error message locators
    LOGIN_ERROR_MSG = (By.CSS_SELECTOR, ".alert-block")


class ProfilePageLocators(object):

    # Profile update input locators
    USERNAME_UPDATE_INPUT = (By.ID, "id_username")
    EMAIL_UPDATE_INPUT = (By.ID, "id_email")
    UPDATE_BUTTON = (By.CSS_SELECTOR, ".btn-outline-info")

    # Success message locators
    UPDATE_SUCCESS_MSG = (By.CSS_SELECTOR, ".alert-success")

    # Error message locators
    USERNAME_UPDATE_ERROR_MSG = (By.ID, "error_1_id_username")