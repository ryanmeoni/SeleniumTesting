import time
import unittest
from page import HomePage, RegisterPage, LoginPage
from testingData import RegisterAndLoginPageTestingData

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/ryan/Desktop/chromedriver"


# Base testing class for setUp() and tearDown() methods
class BaseTesting(unittest.TestCase):
    driver = None

    def setUp(self):
        global PATH
        self.driver = webdriver.Chrome(PATH)
        self.driver.maximize_window()

    def tearDown(self):
        pass
        self.driver.close()


# Tests for the register page
class RegisterPageTests(BaseTesting):

    # Test that correct error message shows when registering with a taken username
    def test_register_existing_user_name(self):
        homePage = HomePage(self.driver)
        homePage.click_register_button()

        registerPage = RegisterPage(homePage.driver)
        registerPage.sign_up(RegisterAndLoginPageTestingData.REGISTERED_USERNAME,
                             RegisterAndLoginPageTestingData.VALID_EMAIL,
                             RegisterAndLoginPageTestingData.MATCHING_PASSWORD_ONE,
                             RegisterAndLoginPageTestingData.MATCHING_PASSWORD_TWO)
        assert registerPage.check_username_error() == 0

    # Test that correct error message shows when the two password fields do not match during registration
    def test_register_not_matching_passwords(self):
        homePage = HomePage(self.driver)
        homePage.click_register_button()

        registerPage = RegisterPage(homePage.driver)
        registerPage.sign_up(RegisterAndLoginPageTestingData.UNREGISTERED_USERNAME,
                             RegisterAndLoginPageTestingData.VALID_EMAIL,
                             RegisterAndLoginPageTestingData.NOT_MATCHING_PASSWORD_ONE,
                             RegisterAndLoginPageTestingData.NOT_MATCHING_PASSWORD_TWO)
        assert registerPage.check_password_no_match_error() == 0


class LoginPageTests(BaseTesting):

    def test_login_successful(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(RegisterAndLoginPageTestingData.REGISTERED_USERNAME,
                        RegisterAndLoginPageTestingData.MATCHING_PASSWORD_ONE)

        redirectHomePage = HomePage(loginPage.driver)
        assert redirectHomePage.check_logged_in() == 0


if __name__ == "__main__":
    unittest.main()