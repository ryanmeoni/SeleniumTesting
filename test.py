# Standard library imports
import unittest

# 3rd party imports
from selenium import webdriver

# Local file imports
from Resources.page import (HomePage, RegisterPage, LoginPage, ProfilePage,
                      CreatePostPage, IndividualPostPage, ConfirmDeletePostPage)

from TestingData.testingData import (HomePageTestingData, RegisterPageTestingData,
                                     LoginPageTestingData, ProfilePageTestingData, CreatePostTestingData)


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
class RegisterPageTests(BaseTest):

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


class LoginPageTests(BaseTest):

    # Test that a registered user can successfully login
    def test_login_successful(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(LoginPageTestingData.REGISTERED_USERNAME,
                        LoginPageTestingData.CORRECT_PASSWORD)

        redirectHomePage = HomePage(loginPage.driver)
        assert redirectHomePage.check_if_logged_in() == 0

    # Test that we cannot log in with a non-existent user
    def test_no_matching_username_during_login(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(LoginPageTestingData.UNREGISTERED_USERNAME,
                        LoginPageTestingData.CORRECT_PASSWORD)

        assert loginPage.check_for_login_error() == 0

    # Test that we cannot successfully login a user with the wrong password
    def test_wrong_password_during_login(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(LoginPageTestingData.REGISTERED_USERNAME,
                        LoginPageTestingData.INCORRECT_PASSWORD)

        assert loginPage.check_for_login_error() == 0


class UserProfileTests(BaseTest):

    # Test that we can successfully update the username of a user
    def test_update_username_success(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(ProfilePageTestingData.ORIGINAL_TEST_USERNAME, ProfilePageTestingData.ORIGINAL_TEST_PASSWORD)

        redirectHomePage = HomePage(loginPage.driver)
        redirectHomePage.click_profile_button()

        profilePage = ProfilePage(redirectHomePage.driver)
        profilePage.set_username(ProfilePageTestingData.NEW_TEST_USERNAME)
        profilePage.click_update_button()
        assert profilePage.check_for_update_profile_success() == 0
        assert profilePage.get_username() == ProfilePageTestingData.NEW_TEST_USERNAME

        # Reset test user with original values, we do not want to keep the updated values so we can reproduce tests.
        profilePage.set_username(ProfilePageTestingData.ORIGINAL_TEST_USERNAME)
        profilePage.click_update_button()
        assert profilePage.check_for_update_profile_success() == 0
        assert profilePage.get_username() == ProfilePageTestingData.ORIGINAL_TEST_USERNAME

    # Test that we can successfully update the email address of a user
    def test_update_email_success(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(ProfilePageTestingData.ORIGINAL_TEST_USERNAME, ProfilePageTestingData.ORIGINAL_TEST_PASSWORD)

        redirectHomePage = HomePage(loginPage.driver)
        redirectHomePage.click_profile_button()

        profilePage = ProfilePage(redirectHomePage.driver)
        profilePage.set_email(ProfilePageTestingData.NEW_TEST_EMAIL)
        profilePage.click_update_button()
        assert profilePage.check_for_update_profile_success() == 0
        assert profilePage.get_email() == ProfilePageTestingData.NEW_TEST_EMAIL

        # Reset test user with original values, we do not want to keep the updated values so we can reproduce tests.
        profilePage.set_email(ProfilePageTestingData.ORIGINAL_TEST_EMAIL)
        profilePage.click_update_button()
        assert profilePage.check_for_update_profile_success() == 0
        assert profilePage.get_email() == ProfilePageTestingData.ORIGINAL_TEST_EMAIL

    # Test that we cannot update a user's username to another user's username
    def test_update_username_error(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(ProfilePageTestingData.ORIGINAL_TEST_USERNAME, ProfilePageTestingData.ORIGINAL_TEST_PASSWORD)

        redirectHomePage = HomePage(loginPage.driver)
        redirectHomePage.click_profile_button()

        profilePage = ProfilePage(redirectHomePage.driver)
        profilePage.set_username(ProfilePageTestingData.CONFLICTING_USERNAME)
        profilePage.click_update_button()

        assert profilePage.check_for_update_profile_username_error() == 0


class CreatePostTests(BaseTest):

    # Test that can successfully create a post
    def test_create_post_success(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(ProfilePageTestingData.ORIGINAL_TEST_USERNAME, ProfilePageTestingData.ORIGINAL_TEST_PASSWORD)

        redirectHomePage = HomePage(loginPage.driver)
        redirectHomePage.click_create_post_button()

        createPostPage = CreatePostPage(redirectHomePage.driver)
        createPostPage.set_post_title(CreatePostTestingData.TEST_POST_TITLE)
        createPostPage.set_post_content(CreatePostTestingData.TEST_POST_CONTENT)
        createPostPage.click_post_button()

        individualPostPage = IndividualPostPage(createPostPage.driver)
        assert individualPostPage.check_for_post_success() == 0

        # Delete this test post so we do not populate application with unnecessary test posts
        individualPostPage.click_delete_post_button()

        confirmDeletePostPage = ConfirmDeletePostPage(individualPostPage.driver)
        confirmDeletePostPage.click_confirm_delete_button()

class UpdatePostTests(BaseTest):

    # Test that ensures a user cannot update a post they do not own
    def test_can_access_own_posts(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(ProfilePageTestingData.ORIGINAL_TEST_USERNAME, ProfilePageTestingData.ORIGINAL_TEST_PASSWORD)

        redirectHomePage = HomePage(loginPage.driver)
        redirectHomePage.click_post_link_by_title(HomePageTestingData.TEST_USER_OWNED_POST_TITLE)

        individualPostPage = IndividualPostPage(redirectHomePage.driver)
        assert individualPostPage.check_if_user_made_post() == 0

    def test_cannot_access_other_user_posts(self):
        homePage = HomePage(self.driver)
        homePage.click_login_button()

        loginPage = LoginPage(homePage.driver)
        loginPage.login(ProfilePageTestingData.ORIGINAL_TEST_USERNAME, ProfilePageTestingData.ORIGINAL_TEST_PASSWORD)

        redirectHomePage = HomePage(loginPage.driver)
        redirectHomePage.click_post_link_by_title(HomePageTestingData.TEST_USER_NOT_OWNED_POST_TITLE)
        individualPostPage = IndividualPostPage(redirectHomePage.driver)
        assert individualPostPage.check_if_user_made_post() == -1


if __name__ == "__main__":
    unittest.main()
