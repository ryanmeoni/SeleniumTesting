import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

PATH = "/home/ryan/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)


def testExistingUser():
    global driver
    driver.get("https://ryanmeoni.pythonanywhere.com/register")

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


def testNotMatchingPasswords():
    global driver
    driver.get("https://ryanmeoni.pythonanywhere.com/register")

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

if __name__ == "__main__":
    testExistingUser()
    testNotMatchingPasswords()