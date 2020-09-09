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

    ORIGINAL_TEST_USERNAME = "test"
    NEW_TEST_USERNAME = "test_Changed_Username"
    CONFLICTING_USERNAME = "ryan"

    ORIGINAL_TEST_EMAIL = "test@gmail.com"
    NEW_TEST_EMAIL = "test_Changed_Email@gmail.com"
    INVALID_EMAIL = "invalid_Email"

    ORIGINAL_TEST_PASSWORD = "thisisatest"

class CreatePostTestingData(object):

    TEST_POST_TITLE = "This is the test post title"
    TEST_POST_CONTENT = "This is the test post content"
