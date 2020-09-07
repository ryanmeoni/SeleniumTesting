import time
import unittest
import page
from testingData import TestingData

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/ryan/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)

# Helper function to login the test user
def helperLogin():
    global driver
    driver.get("https://ryanmeoni.pythonanywhere.com/login/")

    usernameInput = driver.find_element_by_id("id_username")
    passwordInput = driver.find_element_by_id("id_password")

    usernameInput.send_keys("test")
    passwordInput.send_keys("thisisatest")
    passwordInput.send_keys(Keys.RETURN)

    # Wait for 'Your Profile' anchor link to appear after login, wait max 10 seconds
    try:
        loginSuccessElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Your Profile"))

        )
        return 0

    except Exception as E:
        print("Unexpected exception from logging in test user, exception is" + str(E))
        return -1

# TESTS FOR LOGIN PAGE
def testLoginSuccess():
    return helperLogin()


# TESTS FOR REGISTER PAGE
def testRegisterExistingUsername():
    global driver
    driver.get("https://ryanmeoni.pythonanywhere.com/register")

    time.sleep(2)

    # Find fields needed to be populated to register
    usernameInput = driver.find_element_by_id("id_username")
    emailInput = driver.find_element_by_id("id_email")
    passwordInput = driver.find_element_by_id("id_password1")
    passwordConfirmInput = driver.find_element_by_id("id_password2")

    usernameInput.send_keys("ryan")
    emailInput.send_keys("rmeon001@ucr.edu")
    passwordInput.send_keys("matchingPasswords")
    passwordConfirmInput.send_keys("matchingPasswords")

    # Now hit enter on last password field
    passwordConfirmInput.send_keys(Keys.RETURN)
    time.sleep(1)
    try:
        checkResult = driver.find_element_by_id("error_1_id_username")
        return 0

    except NoSuchElementException:
        print("username was valid, should not occur.")
        return -1


def testRegisterNotMatchingPasswords():
    global driver
    driver.get("https://ryanmeoni.pythonanywhere.com/register")

    # Find fields needed to be populated to register
    usernameInput = driver.find_element_by_id("id_username")
    emailInput = driver.find_element_by_id("id_email")
    passwordInput = driver.find_element_by_id("id_password1")
    passwordConfirmInput = driver.find_element_by_id("id_password2")

    usernameInput.send_keys("doesNotMatter")
    emailInput.send_keys("test@gmail.com")
    passwordInput.send_keys("notMatchingPasswords!")
    passwordConfirmInput.send_keys("notMatchingPasswords!!!!!!!")

    passwordConfirmInput.send_keys(Keys.RETURN)
    time.sleep(1)
    try:
        checkResult = driver.find_element_by_id("error_1_id_password2")
        return 0

    except NoSuchElementException:
        print("passwords matched, should not occur in this test.")
        return -1

# Beginning of move to unittest framework
class PythonOrgSearchTest(unittest.TestCase):

    def setUp(self):
        global PATH
        self.driver = webdriver.Chrome(PATH)

    # Working test of taken username during registration
    def test_register_existing_user_name(self):
        registerPage = page.RegisterPage(self.driver)
        registerPage.sign_up(TestingData.TAKEN_USERNAME, TestingData.VALID_EMAIL,
                             TestingData.MATCHING_PASSWORD_ONE, TestingData.MATCHING_PASSWORD_TWO)
        assert registerPage.check_username_error() == 0

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()