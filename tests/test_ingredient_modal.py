
import allure

from pages.main_page import MainPage


@allure.feature("Модальное окно ингредиента")
class TestIngredientModal:

    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_modal(self, driver):
        page = MainPage(driver)

        page.open_main_page()
        page.open_ingredient_modal()

        assert page.is_ingredient_modal_opened()

    @allure.title("Закрытие модального окна ингредиента крестиком")
    def test_close_ingredient_modal(self, driver):
        page = MainPage(driver)

        page.open_main_page()
        page.open_ingredient_modal()
        page.close_ingredient_modal()

        assert page.is_ingredient_modal_closed()
