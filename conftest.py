

import pytest
from selenium import webdriver

from api_client import create_test_user, delete_test_user


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    try:
        browser.set_window_size(1920, 1080)
        yield browser
    finally:
        browser.quit()


@pytest.fixture
def test_user():
    user_data, response = create_test_user()
    access_token = response["accessToken"]

    try:
        yield user_data
    finally:
        delete_test_user(access_token)
