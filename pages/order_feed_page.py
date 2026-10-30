import allure

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from urls import ORDER_FEED_URL


class OrderFeedPage(BasePage):

    @allure.step("Открытие страницы ленты заказов")
    def open_order_feed(self):
        self.open_page(ORDER_FEED_URL)

    @allure.step("Получение общего количества выполненных заказов")
    def get_total_orders(self):
        counter = self.find_element(
            OrderFeedPageLocators.TOTAL_ORDERS_COUNTER
        )
        return int(counter.text.replace(" ", ""))

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders(self):
        counter = self.find_element(
            OrderFeedPageLocators.TODAY_ORDERS_COUNTER
        )
        return int(counter.text.replace(" ", ""))

    @allure.step("Получение номеров заказов в работе")
    def get_in_progress_order_numbers(self):
        return self.get_elements_text(
            OrderFeedPageLocators.IN_PROGRESS_ORDER_NUMBERS
        )