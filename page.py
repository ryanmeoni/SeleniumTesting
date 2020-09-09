from locator import (RegisterPageLocators, LoginPageLocators,
                     HomePageLocators, ProfilePageLocators, CreatePostPageLocators,
                     IndividualPostPageLocators, ConfirmDeletePostPageLocators)

from testingData import HomePageTestingData

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        try:
            currElement = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator))
            currElement.click()
            return 0

        except NoSuchElementException:
            print("No such element in click() in page.py")
            return -1

    def check_element_exists(self, locator):
        try:
            WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator))
            return 0

        except TimeoutException:
            print("Timeout in check_element_exists() in page.py")
            return -1

        except NoSuchElementException:
            print("No such element in check_element_exists() in page.py")
            return -1

    def set_input_text(self, locator, text):
        try:
            self.driver.find_element(*locator).clear()
            currElement = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator))
            currElement.send_keys(text)
            return 0

        except TimeoutException:
            print("Timeout in input_text() in page.py")
            return -1

    def get_input_text(self, locator):
        try:
            currElementText = self.driver.find_element(*locator).get_property("value")
            return currElementText

        except TimeoutException:
            print("Timeout in get_text() in page.py")

        except NoSuchElementException:
            print("No such element in get_text() in page.py")


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(HomePageTestingData.HOMEPAGE_URL)

    def click_login_button(self):
        self.click_element(HomePageLocators.LOGIN_BUTTON)

    def click_register_button(self):
        self.click_element(HomePageLocators.REGISTER_BUTTON)

    def check_if_logged_in(self):
        return self.check_element_exists(HomePageLocators.YOUR_PROFILE_BUTTON)

    def click_profile_button(self):
        self.click_element(HomePageLocators.YOUR_PROFILE_BUTTON)

    def click_create_post_button(self):
        self.click_element(HomePageLocators.CREATE_POST_BUTTON)


class RegisterPage(BasePage):

    def sign_up(self, username, email, passwordOne, passwordTwo):
        self.set_input_text(RegisterPageLocators.USERNAME_INPUT, username)
        self.set_input_text(RegisterPageLocators.EMAIL_INPUT, email)
        self.set_input_text(RegisterPageLocators.PASSWORD_INPUT_ONE, passwordOne)
        self.set_input_text(RegisterPageLocators.PASSWORD_INPUT_TWO, passwordTwo)
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)

    def check_for_username_error(self):
        return self.check_element_exists(RegisterPageLocators.ERROR_USERNAME_CONFLICT_MSG)

    def check_for_password_no_match_error(self):
        return self.check_element_exists(RegisterPageLocators.ERROR_PASSWORDS_NO_MATCH_MSG)


class LoginPage(BasePage):

    def login(self, username, password):
        self.set_input_text(LoginPageLocators.USERNAME_INPUT, username)
        self.set_input_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def check_for_login_error(self):
        return self.check_element_exists(LoginPageLocators.LOGIN_ERROR_MSG)


class ProfilePage(BasePage):

    def update_username(self, username):
        self.set_input_text(ProfilePageLocators.USERNAME_UPDATE_INPUT, username)

    def update_email(self, email):
        self.set_input_text(ProfilePageLocators.EMAIL_UPDATE_INPUT, email)

    def get_username(self):
        return self.get_input_text(ProfilePageLocators.USERNAME_UPDATE_INPUT)

    def get_email(self):
        return self.get_input_text(ProfilePageLocators.EMAIL_UPDATE_INPUT)

    def click_update_button(self):
        self.click_element(ProfilePageLocators.UPDATE_BUTTON)

    def check_for_update_profile_success(self):
        return self.check_element_exists(ProfilePageLocators.UPDATE_SUCCESS_MSG)

    def check_for_update_profile_error(self):
        return self.check_element_exists(ProfilePageLocators.USERNAME_UPDATE_ERROR_MSG)

    def update_picture(self):  # TODO
        pass


class CreatePostPage(BasePage):

    def write_post_title(self, postTitle):
        self.set_input_text(CreatePostPageLocators.POST_TITLE, postTitle)

    def write_post_content(self, postContent):
        self.set_input_text(CreatePostPageLocators.POST_CONTENT, postContent)

    def get_post_title(self):
        return self.get_input_text(CreatePostPageLocators.POST_TITLE)

    def get_post_content(self):
        return self.get_input_text(CreatePostPageLocators.POST_CONTENT)

    def click_post_button(self):
        self.click_element(CreatePostPageLocators.CREATE_POST_BUTTON)


class IndividualPostPage(BasePage):

    def check_for_post_success(self):
        return self.check_element_exists(IndividualPostPageLocators.INDIVIDUAL_POST_UPDATE)

    def click_delete_post_button(self):
        self.click_element(IndividualPostPageLocators.INDIVIDUAL_POST_DELETE)

    def click_update_post_button(self):
        self.click_element(IndividualPostPageLocators.INDIVIDUAL_POST_UPDATE)


class ConfirmDeletePostPage(BasePage):

    def click_confirm_delete_button(self):
        self.click_element(ConfirmDeletePostPageLocators.CONFIRM_DELETE)

    def click_cancel_delete_button(self):
        self.click_element(ConfirmDeletePostPageLocators.CANCEL_DELETE)
