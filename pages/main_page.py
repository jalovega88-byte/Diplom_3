
import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL, ORDER_FEED_URL


class MainPage(BasePage):

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.open_page(BASE_URL)

    @allure.step("Переход в конструктор")
    def click_constructor(self):
        self.click_element(
            MainPageLocators.CONSTRUCTOR_LINK
        )

    @allure.step("Переход в ленту заказов")
    def click_order_feed(self):
        self.click_element(
            MainPageLocators.ORDER_FEED_LINK
        )

    @allure.step("Проверка открытия конструктора")
    def is_constructor_opened(self):
        return self.get_current_url().rstrip("/") == BASE_URL.rstrip("/")

    @allure.step("Проверка открытия ленты заказов")
    def is_order_feed_opened(self):
        return self.get_current_url().rstrip("/") == ORDER_FEED_URL.rstrip("/")
    
    @allure.step("Открытие модального окна ингредиента")
    def open_ingredient_modal(self):
        self.find_element(MainPageLocators.INGREDIENT_CARD)

        self.wait_for_overlays_to_disappear(
            MainPageLocators.MODAL_OVERLAY
        )

        self.click_element(MainPageLocators.INGREDIENT_CARD)


    @allure.step("Проверка открытия модального окна ингредиента")
    def is_ingredient_modal_opened(self):
        return self.find_element(
            MainPageLocators.INGREDIENT_MODAL
        ).is_displayed()

    @allure.step("Закрытие модального окна ингредиента")
    def close_ingredient_modal(self):
        self.click_element(
            MainPageLocators.MODAL_CLOSE_BUTTON
        )

    @allure.step("Проверка закрытия модального окна ингредиента")
    def is_ingredient_modal_closed(self):
        return self.wait_for_invisibility(
            MainPageLocators.INGREDIENT_MODAL
        )

    @allure.step("Получение счётчика ингредиентов")
    def get_ingredient_counter(self):
        counter = self.find_element(
            MainPageLocators.INGREDIENT_COUNTER
        )
        return int(counter.text)


    @allure.step("Перетаскивание начинки в конструктор")
    def drag_ingredient_to_constructor(self):
        counter_before = self.get_ingredient_counter()

        self.drag_and_drop(
            MainPageLocators.FILLING_CARD,
            MainPageLocators.BURGER_CONSTRUCTOR
        )

        self.wait_for_condition(
            lambda driver: self.get_ingredient_counter() > counter_before,
            message="Приложение не добавило ингредиент после drag-and-drop"
        )


    @allure.step("Нажатие на кнопку оформления заказа")
    def click_place_order(self):
        self.click_element(
            MainPageLocators.PLACE_ORDER_BUTTON
        )


    @allure.step("Получение номера оформленного заказа")
    def get_order_number(self):
        return self.wait_for_order_number(
            MainPageLocators.ORDER_NUMBER
        )


    @allure.step("Нажатие на кнопку «Войти в аккаунт»")
    def click_login_button(self):
        self.click_element(
            MainPageLocators.LOGIN_BUTTON
        )


    @allure.step("Перетаскивание булки в конструктор")
    def drag_bun_to_constructor(self):
        self.drag_and_drop(
            MainPageLocators.BUN_INGREDIENT,
            MainPageLocators.BURGER_CONSTRUCTOR
        )

        
    @allure.step("Проверка наличия булки в конструкторе")
    def is_bun_in_constructor(self):
        return self.find_element(
            MainPageLocators.BUN_IN_CONSTRUCTOR
        ).is_displayed()
