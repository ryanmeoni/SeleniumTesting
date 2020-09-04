import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/ryan/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)


# TESTS FOR LOGIN PAGE

def testLoginSuccess():
    global driver
    driver.get("https://ryanmeoni.pythonanywhere.com/login/")

    usernameInput = driver.find_element_by_id("id_username")
    passwordInput = driver.find_element_by_id("id_password")

    usernameInput.send_keys("test")
    passwordInput.send_keys("thisisatest")
    passwordInput.send_keys(Keys.RETURN)

    # Wait 10 seconds max for login to occur
    try:
        loginSuccessElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Your Profile"))
        )
    except Exception as E:
        print("Unexpected exception in testLoginSuccess, exception is" + str(E))
        return -1


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

    except NoSuchElementException:
        print("passwords matched, should not occur in this test.")
        return -1


if __name__ == "__main__":
    testRegisterExistingUsername()
    testRegisterNotMatchingPasswords()
    testLoginSuccess()