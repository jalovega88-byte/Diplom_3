
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL, ORDER_FEED_URL


class MainPage(BasePage):

    def open_main_page(self):
        self.open_page(BASE_URL)

    def click_constructor(self):
        self.click_element(
            MainPageLocators.CONSTRUCTOR_LINK
        )

    def click_order_feed(self):
        self.click_element(
            MainPageLocators.ORDER_FEED_LINK
        )

    def is_constructor_opened(self):
        return self.driver.current_url.rstrip("/") == BASE_URL.rstrip("/")

    def is_order_feed_opened(self):
        return self.driver.current_url.rstrip("/") == ORDER_FEED_URL.rstrip("/")

    
    def open_ingredient_modal(self):
        self.find_element(MainPageLocators.INGREDIENT_CARD)

        self.wait.until(
            lambda driver: all(
                not overlay.is_displayed()
                for overlay in driver.find_elements(
                    *MainPageLocators.MODAL_OVERLAY
                )
            ),
            message="Перекрывающий слой не исчез перед кликом по ингредиенту",
        )

        self.click_element(MainPageLocators.INGREDIENT_CARD)

    def is_ingredient_modal_opened(self):
        return self.find_element(
            MainPageLocators.INGREDIENT_MODAL
        ).is_displayed()

    def close_ingredient_modal(self):
        self.click_element(
            MainPageLocators.MODAL_CLOSE_BUTTON
        )

    def is_ingredient_modal_closed(self):
        from selenium.webdriver.support import expected_conditions as EC

        return self.wait.until(
            EC.invisibility_of_element_located(
                MainPageLocators.INGREDIENT_MODAL
            )
        )
    
    def get_ingredient_counter(self):
        counter = self.find_element(
            MainPageLocators.INGREDIENT_COUNTER
        )
        return int(counter.text)

    
    
    def drag_ingredient_to_constructor(self):
        counter_before = self.get_ingredient_counter()

        ingredient = self.find_element(
            MainPageLocators.FILLING_CARD
        )
        constructor = self.find_element(
            MainPageLocators.BURGER_CONSTRUCTOR
        )

        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            function fire(element, type) {
                const rect = element.getBoundingClientRect();

                element.dispatchEvent(new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer,
                    clientX: rect.left + rect.width / 2,
                    clientY: rect.top + rect.height / 2
                }));
            }

            source.scrollIntoView({block: "center"});
            fire(source, "dragstart");
            fire(target, "dragenter");
            fire(target, "dragover");
            fire(target, "drop");
            fire(source, "dragend");
        """, ingredient, constructor)

        self.wait.until(
            lambda driver: self.get_ingredient_counter() > counter_before,
            message="Приложение не добавило ингредиент после drag-and-drop",
        )

        
    def click_place_order(self):
        self.click_element(
            MainPageLocators.PLACE_ORDER_BUTTON
        )

        
        
    def get_order_number(self):
        def number_is_ready(driver):
            element = driver.find_element(
                *MainPageLocators.ORDER_NUMBER
            )

            number = element.text.strip()

            if number.isdigit() and number != "9999":
                return number

            return False

        return self.wait.until(
            number_is_ready,
            message="Настоящий номер заказа не появился"
        )


        
    def click_login_button(self):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import ElementClickInterceptedException

        def click_when_ready(driver):
            try:
                button = driver.find_element(
                    *MainPageLocators.LOGIN_BUTTON
                )

                if not button.is_displayed() or not button.is_enabled():
                    return False

                button.click()
                return True

            except ElementClickInterceptedException:
                return False

        self.wait.until(
            click_when_ready,
            message="Кнопка входа осталась перекрытой"
        )


        
    def drag_bun_to_constructor(self):
        bun = self.find_element(MainPageLocators.BUN_INGREDIENT)
        constructor = self.find_element(MainPageLocators.BURGER_CONSTRUCTOR)

        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            function fire(element, type) {
                const rect = element.getBoundingClientRect();

                element.dispatchEvent(new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer,
                    clientX: rect.left + rect.width / 2,
                    clientY: rect.top + rect.height / 2
                }));
            }

            source.scrollIntoView({block: "center"});

            fire(source, "dragstart");
            fire(target, "dragenter");
            fire(target, "dragover");
            fire(target, "drop");
            fire(source, "dragend");
        """, bun, constructor)


        
    def is_bun_in_constructor(self):
        from selenium.webdriver.support import expected_conditions as EC

        return self.wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.BUN_IN_CONSTRUCTOR
            )
        )



