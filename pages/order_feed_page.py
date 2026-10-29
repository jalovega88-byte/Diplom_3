
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from urls import ORDER_FEED_URL
from selenium.common.exceptions import StaleElementReferenceException


class OrderFeedPage(BasePage):

    def open_order_feed(self):
        self.open_page(ORDER_FEED_URL)

    def get_total_orders(self):
        counter = self.find_element(
            OrderFeedPageLocators.TOTAL_ORDERS_COUNTER
        )
        return int(counter.text.replace(" ", ""))

    def get_today_orders(self):
        counter = self.find_element(
            OrderFeedPageLocators.TODAY_ORDERS_COUNTER
        )
        return int(counter.text.replace(" ", ""))

       
    def get_in_progress_order_numbers(self):
        try:
            elements = self.driver.find_elements(
                *OrderFeedPageLocators.IN_PROGRESS_ORDER_NUMBERS
            )

            return [
                element.text.strip()
                for element in elements
            ]

        except StaleElementReferenceException:
            return []
 

    
