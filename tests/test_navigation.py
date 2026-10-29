
import allure

from pages.main_page import MainPage


@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Переход в Конструктор")
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)

        page.open_main_page()
        page.click_order_feed()
        page.click_constructor()

        assert page.is_constructor_opened()

    @allure.title("Переход в Ленту заказов")
    def test_go_to_order_feed(self, driver):
        page = MainPage(driver)

        page.open_main_page()
        page.click_order_feed()

        assert page.is_order_feed_opened()
