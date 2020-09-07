
from locator import RegisterPageLocators
from testingData import TestingData

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

    def input_text(self, locator, text):
        try:
            currElement = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            currElement.send_keys(text)
            return 0

        except TimeoutException:
            print("Timeout in input_text() in page.py")
            return -1


class RegisterPage(BasePage):

    def sign_up(self, username, email, passwordOne, passwordTwo):
        self.driver.get("https://ryanmeoni.pythonanywhere.com/register")
        self.input_text(RegisterPageLocators.USERNAME_INPUT, username)
        self.input_text(RegisterPageLocators.EMAIL_INPUT, email)
        self.input_text(RegisterPageLocators.PASSWORD_INPUT_ONE, passwordOne)
        self.input_text(RegisterPageLocators.PASSWORD_INPUT_TWO, passwordTwo)
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)

    def check_username_error(self):
        return self.check_element_exists(RegisterPageLocators.USERNAME_CONFLICT_ERROR_MSG)
