# Third party imports
from selenium.webdriver.common.by import By


class HomePageLocators(object):

    # General locators
    LOGIN_BUTTON = (By.LINK_TEXT, "Login")
    REGISTER_BUTTON = (By.LINK_TEXT, "Register")
    YOUR_PROFILE_BUTTON = (By.LINK_TEXT, "Your Profile")
    CREATE_POST_BUTTON = (By.LINK_TEXT, "Create Post")
    MAIN_LOCATOR = (By.CSS_SELECTOR, "main")

    # Test post locators
    TEST_POST_LINK = (By.LINK_TEXT, "Hello")


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
    PICTURE_UPDATE_INPUT = (By.ID, "id_image")
    UPDATE_BUTTON = (By.CSS_SELECTOR, ".btn-outline-info")

    # Success message locators
    UPDATE_SUCCESS_MSG = (By.CSS_SELECTOR, ".alert-success")

    # Error message locators
    USERNAME_UPDATE_ERROR_MSG = (By.ID, "error_1_id_username")
    PICTURE_UPDATE_ERROR_MSG = (By.ID, "error_1_id_image")


class CreatePostPageLocators(object):

    # Post creation input locators
    POST_TITLE = (By.ID, "id_title")
    POST_CONTENT = (By.ID, "id_content")
    CREATE_POST_BUTTON = (By.CSS_SELECTOR, ".btn-outline-info")


class IndividualPostPageLocators(object):

    # General locators
    MAIN_LOCATOR = (By.CSS_SELECTOR, "main")

    # Post update and delete button locators (only visible when post was made by logged in user)
    INDIVIDUAL_POST_UPDATE = (By.CSS_SELECTOR, ".btn-info")
    INDIVIDUAL_POST_DELETE = (By.CSS_SELECTOR, ".btn-danger")


class ConfirmDeletePostPageLocators(object):

    # Cancel deletion and confirm deletetion button locators
    CONFIRM_DELETE = (By.CSS_SELECTOR, ".btn-outline-danger")
    CANCEL_DELETE = (By.CSS_SELECTOR, "btn-outline-info")
