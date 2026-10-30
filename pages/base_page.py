import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)

class BasePage:
    @allure.step("Инициализация базовой страницы")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открытие страницы: {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Нажатие на элемент: {locator}")
    def click_element(self, locator):
        def click_when_ready(driver):
            try:
                element = driver.find_element(*locator)

                if not element.is_displayed() or not element.is_enabled():
                    return False

                element.click()
                return True

            except ElementClickInterceptedException:
                return False

        self.wait.until(
            click_when_ready,
            message=f"Не удалось нажать на элемент: {locator}"
        )

    @allure.step("Поиск видимого элемента: {locator}")
    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Получение текущего URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Перетаскивание элемента из {source_locator} в {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

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
        """, source, target)

    @allure.step("Ожидание исчезновения элемента: {locator}")
    def wait_for_invisibility(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Ожидание выполнения условия")
    def wait_for_condition(self, condition, message):
        return self.wait.until(
            condition,
            message=message
        )

    @allure.step("Ожидание исчезновения всех перекрывающих элементов")
    def wait_for_overlays_to_disappear(self, locator):
        return self.wait.until(
            lambda driver: all(
                not overlay.is_displayed()
                for overlay in driver.find_elements(*locator)
            ),
            message="Перекрывающий слой не исчез"
        )

    @allure.step("Ожидание появления настоящего номера заказа")
    def wait_for_order_number(self, locator):
        def number_is_ready(driver):
            element = driver.find_element(*locator)
            number = element.text.strip()

            if number.isdigit() and number != "9999":
                return number

            return False

        return self.wait.until(
            number_is_ready,
            message="Настоящий номер заказа не появился"
        )

    @allure.step("Ввод текста в поле: {locator}")
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элементов: {locator}")
    def get_elements_text(self, locator):
        try:
            elements = self.driver.find_elements(*locator)

            return [
                element.text.strip()
                for element in elements
            ]

        except StaleElementReferenceException:
            return []