

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

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
import allure


@pytest.fixture
def create_order_and_get_counters(driver, test_user):
    feed_page = OrderFeedPage(driver)
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    with allure.step("Получить значения счётчиков до оформления заказа"):
        feed_page.open_order_feed()
        total_before = feed_page.get_total_orders()
        today_before = feed_page.get_today_orders()

    with allure.step("Авторизоваться"):
        main_page.open_main_page()
        main_page.click_login_button()

        login_page.login(
            test_user["email"],
            test_user["password"]
        )

    with allure.step("Оформить новый заказ"):
        main_page.drag_bun_to_constructor()
        main_page.is_bun_in_constructor()
        main_page.click_place_order()
        main_page.get_order_number()

    with allure.step("Открыть ленту заказов"):
        feed_page.open_order_feed()

    return feed_page, total_before, today_before

