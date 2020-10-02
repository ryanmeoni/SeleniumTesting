# Standard library imports
import os

# Third party imports
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Local file imports
from Resources.locator import (RegisterPageLocators, LoginPageLocators,
                      HomePageLocators, ProfilePageLocators, CreatePostPageLocators,
                      IndividualPostPageLocators, ConfirmDeletePostPageLocators, AboutPageLocators)

from TestingData.testingData import HomePageTestingData


# Base class that all page classes inherit from
class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    # Function for clicking an element (such as a button or anchor tag)
    def click_element(self, locator):
        try:
            self.wait_until_element_exists(locator)
            currElement = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator))
            currElement.click()
            return 0

        except NoSuchElementException:
            print("No such element in click() in page.py")
            return -1

    # Function for checking if an element exists on a page
    def wait_until_element_exists(self, locator):
        try:
            WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator))
            return 0

        except TimeoutException:
            print("Timeout in check_element_exists() in page.py")
            return -1

    # Function that checks if an element exists on a page
    def check_if_element_exists(self, locator):
        try:
            self.driver.find_element(*locator)
            return 0

        except NoSuchElementException:
            return -1

    # Function for inputting text into a text field
    def set_input_text(self, locator, text):
        try:
            self.wait_until_element_exists(locator)
            self.driver.find_element(*locator).clear()
            currElement = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator))
            currElement.send_keys(text)
            return 0

        except TimeoutException:
            print("Timeout in input_text() in page.py")
            return -1

    # Function for retrieving text from a text field
    def get_input_text(self, locator):
        try:
            self.wait_until_element_exists(locator)
            currElementText = self.driver.find_element(*locator).get_property("value")
            return currElementText

        except TimeoutException:
            print("Timeout in get_text() in page.py")

        except NoSuchElementException:
            print("No such element in get_text() in page.py")

    # Function that returns all HTML article elements on pages where a list of posts are shown
    def get_all_posts(self):
        try:
            self.wait_until_element_exists(HomePageLocators.MAIN_LOCATOR)
            main = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located(HomePageLocators.MAIN_LOCATOR))
            articles = main.find_elements_by_tag_name("article")
            return articles

        except TimeoutException:
            print("Timeout in get_all_posts() in page.py")

        except NoSuchElementException:
            print("No such element in get_all_posts() in page.py")

    # Function that clicks a post's title link that goes to that individual post
    def click_post_link_by_title(self, postTitle):
        try:
            postLocator = (By.LINK_TEXT, postTitle)
            self.wait_until_element_exists(postLocator)
            self.click_element(postLocator)

        except TimeoutException:
            print("Timeout in click_post_link_by_title")

    # Function that inputs a picture into a picture file upload, does not submit picture or make changes
    def choose_image_file_upload(self, locator, pictureName):
        try:
            self.wait_until_element_exists(locator)
            # os.getcwd() returns the directory where the process was started, which is where test.py is located
            self.driver.find_element(*locator).send_keys(os.getcwd() + pictureName)

        except TimeoutException:
            print("Timeout in choose_image_file_upload in page.py")

        except NoSuchElementException:
            print("No such element in choose_image_file_upload() in page.py")

    def click_about_page_button(self):
        self.click_element(HomePageLocators.ABOUT_BUTTON)


class HomePage(BasePage):
    # Constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(HomePageTestingData.HOMEPAGE_URL)

    # Function that clicks the 'Login' button in top right corner of homepage
    def click_login_button(self):
        self.click_element(HomePageLocators.LOGIN_BUTTON)

    # Function that clicks the 'Register' button in top right corner of homepage
    def click_register_button(self):
        self.click_element(HomePageLocators.REGISTER_BUTTON)

    # Function that checks for the presence of 'Your Profile' button in nav bar, indicating a user is logged in
    def check_if_logged_in(self):
        return self.wait_until_element_exists(HomePageLocators.YOUR_PROFILE_BUTTON)

    # Function that clicks the 'Your Profile' button in top right corner of homepage
    def click_profile_button(self):
        self.click_element(HomePageLocators.YOUR_PROFILE_BUTTON)

    # Function that clicks the 'Create Post' button in top right corner of homepage
    def click_create_post_button(self):
        self.click_element(HomePageLocators.CREATE_POST_BUTTON)


class RegisterPage(BasePage):
    # Function that registers a user
    def sign_up(self, username, email, passwordOne, passwordTwo):
        self.set_input_text(RegisterPageLocators.USERNAME_INPUT, username)
        self.set_input_text(RegisterPageLocators.EMAIL_INPUT, email)
        self.set_input_text(RegisterPageLocators.PASSWORD_INPUT_ONE, passwordOne)
        self.set_input_text(RegisterPageLocators.PASSWORD_INPUT_TWO, passwordTwo)
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)

    # Function that checks for error message generated during registration caused by bad username
    def check_for_username_error(self):
        return self.wait_until_element_exists(RegisterPageLocators.ERROR_USERNAME_CONFLICT_MSG)

    # Function that checks for error message generated during registration caused by unmatched passwords
    def check_for_password_no_match_error(self):
        return self.wait_until_element_exists(RegisterPageLocators.ERROR_PASSWORDS_NO_MATCH_MSG)


class LoginPage(BasePage):

    # Function that logs in a user
    def login(self, username, password):
        self.set_input_text(LoginPageLocators.USERNAME_INPUT, username)
        self.set_input_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    # Function that checks for login error message indicating bad login attempt
    def check_for_login_error(self):
        return self.wait_until_element_exists(LoginPageLocators.LOGIN_ERROR_MSG)


class ProfilePage(BasePage):

    # Function that sets username text field
    def set_username(self, username):
        self.set_input_text(ProfilePageLocators.USERNAME_UPDATE_INPUT, username)

    # Function that sets email text field
    def set_email(self, email):
        self.set_input_text(ProfilePageLocators.EMAIL_UPDATE_INPUT, email)

    # Functions that gets username text field value
    def get_username(self):
        return self.get_input_text(ProfilePageLocators.USERNAME_UPDATE_INPUT)

    # Function that gets email text field value
    def get_email(self):
        return self.get_input_text(ProfilePageLocators.EMAIL_UPDATE_INPUT)

    # Function that clicks the 'Update Profile' button
    def click_update_button(self):
        self.click_element(ProfilePageLocators.UPDATE_BUTTON)

    # Function that checks for success message indicating profile was successfully updated
    def check_for_update_profile_success(self):
        return self.wait_until_element_exists(ProfilePageLocators.UPDATE_SUCCESS_MSG)

    # Function that checks for the error message indicating error updating username on profile page
    def check_for_update_profile_username_error(self):
        return self.wait_until_element_exists(ProfilePageLocators.USERNAME_UPDATE_ERROR_MSG)

    # Function that sets the picture to be updated to on a user's profile page, does not click 'Update Profile'
    def choose_new_profile_picture(self, pictureName):  # TODO
        self.choose_image_file_upload(ProfilePageLocators.PICTURE_UPDATE_INPUT, pictureName)

    # Function that checks for success of update profile picture
    def check_for_update_profile_picture_success(self): # TODO
        return self.wait_until_element_exists(ProfilePageLocators.UPDATE_SUCCESS_MSG)

    # Function that checks for error message indicating error updating user profile picture
    def check_for_update_profile_picture_error(self): # TODO
        return self.wait_until_element_exists(ProfilePageLocators.PICTURE_UPDATE_ERROR_MSG)


class CreatePostPage(BasePage):

    # Function that sets post title text field
    def set_post_title(self, postTitle):
        self.set_input_text(CreatePostPageLocators.POST_TITLE, postTitle)

    # Function that sets post content text field
    def set_post_content(self, postContent):
        self.set_input_text(CreatePostPageLocators.POST_CONTENT, postContent)

    # Functions that gets post title text field value
    def get_post_title(self):
        return self.get_input_text(CreatePostPageLocators.POST_TITLE)

    # Functions that gets post content text field value
    def get_post_content(self):
        return self.get_input_text(CreatePostPageLocators.POST_CONTENT)

    # Function that clicks on the 'Post' button
    def click_post_button(self):
        self.click_element(CreatePostPageLocators.CREATE_POST_BUTTON)


class IndividualPostPage(BasePage):

    # Function that checks for success of making post
    def check_for_post_success(self):
        return self.wait_until_element_exists(IndividualPostPageLocators.INDIVIDUAL_POST_UPDATE)

    # Function that clicks the 'Delete Post' button
    def click_delete_post_button(self):
        self.click_element(IndividualPostPageLocators.INDIVIDUAL_POST_DELETE)

    # Function that clicks the 'Update Post' button
    def click_update_post_button(self):
        self.click_element(IndividualPostPageLocators.INDIVIDUAL_POST_UPDATE)

    # Function that checks if the logged in user made this post (checks for 'Delete Post' and 'Update Post' buttons)
    def check_if_user_made_post(self):
        # Wait for 'main' tag to appear
        self.wait_until_element_exists(IndividualPostPageLocators.MAIN_LOCATOR)

        postUpdateButtonStatus = self.check_if_element_exists(IndividualPostPageLocators.INDIVIDUAL_POST_UPDATE)
        postDeleteButtonStatus = self.check_if_element_exists(IndividualPostPageLocators.INDIVIDUAL_POST_DELETE)

        # Check if the 'Update Post' or 'Delete Post' buttons were not present
        if postDeleteButtonStatus == -1 or postUpdateButtonStatus == -1:
            return -1

        # Otherwise they both are present
        return 0


class ConfirmDeletePostPage(BasePage):

    # Function that clicks the 'Confirm Delete' button
    def click_confirm_delete_button(self):
        self.click_element(ConfirmDeletePostPageLocators.CONFIRM_DELETE)

    # Function that clicks the 'Cancel Delete' button
    def click_cancel_delete_button(self):
        self.click_element(ConfirmDeletePostPageLocators.CANCEL_DELETE)


class AboutPage(BasePage):

    # Function that checks if the page successfully loads
    def check_for_about_page_info(self):
        return self.wait_until_element_exists(AboutPageLocators.ABOUT_PAGE_INFO_XPATH)
