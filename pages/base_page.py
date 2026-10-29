
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_page(self, url):
        self.driver.get(url)

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

    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
