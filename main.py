import time
import unittest
from page import HomePage, RegisterPage, LoginPage, ProfilePage
from testingData import RegisterPageTestingData, LoginPageTestingData, ProfilePageTestingData
from selenium import webdriver

PATH = "/home/ryan/Desktop/chromedriver"


# Base testing class for setUp() and tearDown() methods
class BaseTest(unittest.TestCase):
    driver = None

    def setUp(self):
        global PATH
        self.driver = webdriver.Chrome(PATH)
        self.driver.maximize_window()

    def tearDown(self):
        pass
        self.driver.close()


# Tests for logging in and updating user information
class UserAccessibilityTests(BaseTest):

    # Test that correct error message shows when registering with a taken username
    def test_register_existing_user_name(self):
        homePage = HomePage(self.driver)
        homePage.click_register_button()

        registerPage = RegisterPage(homePage.driver)
        registerPage.sign_up(RegisterPageTestingData.REGISTERED_USERNAME,
                             RegisterPageTestingData.VALID_EMAIL,
                             RegisterPageTestingData.MATCHING_PASSWORD_ONE,
                             RegisterPageTestingData.MATCHING_PASSWORD_TWO)
        assert registerPage.check_for_username_error() == 0

    # Test that correct error message shows when the two password fields do not match during registration
    def test_register_not_matching_passwords(self):
        homePage = HomePage(self.driver)
        homePage.click_register_button()

        registerPage = RegisterPage(homePage.driver)
        registerPage.sign_up(RegisterPageTestingData.UNREGISTERED_USERNAME,
                             RegisterPageTestingData.VALID_EMAIL,
                             RegisterPageTestingData.NOT_MATCHING_PASSWORD_ONE,
                             RegisterPageTestingData.NOT_MATCHING_PASSWORD_TWO)
        assert registerPage.check_for_password_no_match_error() == 0

    def test_login_successful(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(LoginPageTestingData.REGISTERED_USERNAME,
                        LoginPageTestingData.CORRECT_PASSWORD)

        redirectHomePage = HomePage(loginPage.driver)
        assert redirectHomePage.check_if_logged_in() == 0

    def test_no_matching_username_during_login(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(LoginPageTestingData.UNREGISTERED_USERNAME,
                        LoginPageTestingData.CORRECT_PASSWORD)

        assert loginPage.check_for_login_error() == 0

    def test_wrong_password_during_login(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(LoginPageTestingData.REGISTERED_USERNAME,
                        LoginPageTestingData.INCORRECT_PASSWORD)

        assert loginPage.check_for_login_error() == 0

    def test_update_username_success(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(ProfilePageTestingData.ORIGINAL_USERNAME, ProfilePageTestingData.ORIGINAL_PASSWORD)

        redirectHomePage = HomePage(loginPage.driver)
        redirectHomePage.click_profile_button()

        profilePage = ProfilePage(redirectHomePage.driver)
        profilePage.update_username(ProfilePageTestingData.NEW_TEST_USERNAME)
        profilePage.update_email(ProfilePageTestingData.NEW_TEST_EMAIL)
        profilePage.click_update_button()
        assert profilePage.check_for_update_profile_success() == 0

        # Update test user with original values, we do not want to keep the updated values.
        profilePage.update_username(ProfilePageTestingData.ORIGINAL_USERNAME)
        profilePage.update_email(ProfilePageTestingData.ORIGINAL_EMAIL)
        profilePage.click_update_button()
        assert profilePage.check_for_update_profile_success() == 0




if __name__ == "__main__":
    unittest.main()
