
import allure
import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage


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


@allure.feature("Лента заказов")
class TestOrderFeedCounters:

    @allure.title("Увеличение счётчика «Выполнено за всё время»")
    def test_total_orders_counter_increases(self, create_order_and_get_counters):
        feed_page, total_before, _ = create_order_and_get_counters

        with allure.step("Проверить увеличение общего счётчика"):
            assert feed_page.wait.until(
                lambda driver: feed_page.get_total_orders() > total_before,
                message="Счётчик «Выполнено за всё время» не увеличился"
            )

    @allure.title("Увеличение счётчика «Выполнено за сегодня»")
    def test_today_orders_counter_increases(self, create_order_and_get_counters):
        feed_page, _, today_before = create_order_and_get_counters

        with allure.step("Проверить увеличение счётчика за сегодня"):
            assert feed_page.wait.until(
                lambda driver: feed_page.get_today_orders() > today_before,
                message="Счётчик «Выполнено за сегодня» не увеличился"
            )
