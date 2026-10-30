import allure


@allure.feature("Лента заказов")
class TestOrderFeedCounters:

    @allure.title("Увеличение счётчика «Выполнено за всё время»")
    def test_total_orders_counter_increases(self, create_order_and_get_counters):
        feed_page, total_before, _ = create_order_and_get_counters

        with allure.step("Проверить увеличение общего счётчика"):
            assert feed_page.wait_for_condition(
                lambda driver: feed_page.get_total_orders() > total_before,
                message="Счётчик «Выполнено за всё время» не увеличился"
            )

    @allure.title("Увеличение счётчика «Выполнено за сегодня»")
    def test_today_orders_counter_increases(self, create_order_and_get_counters):
        feed_page, _, today_before = create_order_and_get_counters

        with allure.step("Проверить увеличение счётчика за сегодня"):
            assert feed_page.wait_for_condition(
                lambda driver: feed_page.get_today_orders() > today_before,
                message="Счётчик «Выполнено за сегодня» не увеличился"
            )