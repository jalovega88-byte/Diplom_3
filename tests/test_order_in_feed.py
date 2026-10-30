
import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderInFeed:

    @allure.title("Номер оформленного заказа появляется в разделе «В работе»")
    def test_order_appears_in_feed(self, driver, test_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = OrderFeedPage(driver)

        main_page.open_main_page()
        main_page.click_login_button()

        login_page.login(
            test_user["email"],
            test_user["password"]
        )

        main_page.drag_bun_to_constructor()
        main_page.is_bun_in_constructor()

        main_page.click_place_order()
        order_number = main_page.get_order_number()

        feed_page.open_order_feed()

        def order_is_in_progress(browser):
            numbers = feed_page.get_in_progress_order_numbers()

            return order_number in [
                number.lstrip("0") or "0"
                for number in numbers
            ]

        assert feed_page.wait_for_condition(
            order_is_in_progress,
            message=f"Заказ №{order_number} не появился в разделе «В работе»"
        )
