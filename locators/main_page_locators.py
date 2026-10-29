
from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[.//p[text()='Конструктор']]"
    )

    ORDER_FEED_LINK = (
        By.XPATH,
        "//a[.//p[text()='Лента Заказов']]"
    )

    INGREDIENT_CARD = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]"
    )

    INGREDIENT_MODAL = (
        By.XPATH,
        "//h2[contains(text(), 'Детали ингредиента')]"
    )

    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close')]"
    )

    INGREDIENT_COUNTER = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient')])[last()]//p[contains(@class, 'counter_counter__num')]"
    )

    BURGER_CONSTRUCTOR = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor_basket')]"
    )

    FILLING_CARD = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient')])[last()]"
    )

    MODAL_OVERLAY = (
        By.CSS_SELECTOR,
        "div[class*='Modal_modal_overlay']"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти в аккаунт']"
    )

    # Кнопка оформления заказа
    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Оформить заказ']"
    )

    # Первая булочка в списке ингредиентов
    BUN_INGREDIENT = (
        By.XPATH,
        "(//h2[text()='Булки']/following::a[contains(@class, 'BurgerIngredient_ingredient')])[1]"
    )

    # Верхняя булочка в конструкторе
    BUN_IN_CONSTRUCTOR = (
        By.XPATH,
        "//div[contains(@class, 'constructor-element_pos_top')]"
    )

    # Номер заказа в модальном окне
    ORDER_NUMBER = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title')]"
    )

