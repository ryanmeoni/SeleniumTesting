
from locator import RegisterPageLocators, LoginPageLocators, HomePageLocators
from testingData import HomePageTestingData

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        try:
            currElement = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            currElement.click()
            return 0

        except NoSuchElementException:
            print("No such element in click() in page.py")
            return -1

    def check_element_exists(self, locator):
        try:
            currElement = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return 0

        except TimeoutException:
            print("Timeout in check_element_exists() in page.py")
            return -1

        except NoSuchElementException:
            print("No such element in check_element_exists() in page.py")
            return -1

    def input_text(self, locator, text):
        try:
            currElement = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            currElement.send_keys(text)
            return 0

        except TimeoutException:
            print("Timeout in input_text() in page.py")
            return -1


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(HomePageTestingData.HOMEPAGE_URL)

    def click_login_button(self):
        self.click_element(HomePageLocators.LOGIN_BUTTON)

    def click_register_button(self):
        self.click_element(HomePageLocators.REGISTER_BUTTON)

    def check_logged_in(self):
        return self.check_element_exists(HomePageLocators.YOUR_PROFILE_BUTTON)


class RegisterPage(BasePage):

    def sign_up(self, username, email, passwordOne, passwordTwo):
        self.input_text(RegisterPageLocators.USERNAME_INPUT, username)
        self.input_text(RegisterPageLocators.EMAIL_INPUT, email)
        self.input_text(RegisterPageLocators.PASSWORD_INPUT_ONE, passwordOne)
        self.input_text(RegisterPageLocators.PASSWORD_INPUT_TWO, passwordTwo)
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)

    def check_username_error(self):
        return self.check_element_exists(RegisterPageLocators.ERROR_USERNAME_CONFLICT_MSG)

    def check_password_no_match_error(self):
        return self.check_element_exists(RegisterPageLocators.ERROR_PASSWORDS_NO_MATCH_MSG)


class LoginPage(BasePage):

    def login(self, username, password):
        self.input_text(LoginPageLocators.USERNAME_INPUT, username)
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
