
from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    # Счётчик заказов за всё время
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']"
        "/following-sibling::p"
    )

    # Счётчик заказов за сегодня
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']"
        "/following-sibling::p"
    )

    # Номера заказов в разделе «В работе»
    IN_PROGRESS_ORDER_NUMBERS = (
        By.XPATH,
        "//*[text()='В работе:']"
        "/following-sibling::ul/li"
    )
