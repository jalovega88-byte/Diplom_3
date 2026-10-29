
import allure

from pages.main_page import MainPage


@allure.feature("Конструктор")
class TestIngredientCounter:

    @allure.title("Увеличение счётчика при добавлении ингредиента")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        page.open_main_page()

        counter_before = page.get_ingredient_counter()

        page.drag_ingredient_to_constructor()

        counter_after = page.get_ingredient_counter()

        assert counter_after > counter_before, (
            f"Счётчик не увеличился: "
            f"до = {counter_before}, после = {counter_after}"
        )
