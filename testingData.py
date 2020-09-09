class HomePageTestingData(object):

    HOMEPAGE_URL = "https://ryanmeoni.pythonanywhere.com/"


class RegisterPageTestingData(object):

    REGISTERED_USERNAME = "test"
    UNREGISTERED_USERNAME = "bob"

    VALID_EMAIL = "valid@gmail.com"

    MATCHING_PASSWORD_ONE = "thisisatest"
    MATCHING_PASSWORD_TWO = "thisisatest"
    NOT_MATCHING_PASSWORD_ONE = "thisisatest!!"
    NOT_MATCHING_PASSWORD_TWO = "thisisatest!!!!!!!!!!!!!!!"


class LoginPageTestingData(object):

    REGISTERED_USERNAME = "test"
    UNREGISTERED_USERNAME = "bob"

    CORRECT_PASSWORD = "thisisatest"
    INCORRECT_PASSWORD = "thisisatest!!!!!!!!!!!"

class ProfilePageTestingData(object):

    ORIGINAL_USERNAME = "test"
    NEW_TEST_USERNAME = "test-Changed-Username"

    ORIGINAL_EMAIL = "valid@yahoo.com"
    NEW_TEST_EMAIL = "testingChangedEmail@yahoo.com"

    ORIGINAL_PASSWORD = "thisisatest"

