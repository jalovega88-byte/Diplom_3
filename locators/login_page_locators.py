
from selenium.webdriver.common.by import By


class LoginPageLocators:

    # Поле Email
    EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input"
    )

    # Поле пароля
    PASSWORD_INPUT = (
        By.XPATH,
        "//label[text()='Пароль']/following-sibling::input"
    )

    # Кнопка «Войти»
    LOGIN_SUBMIT_BUTTON = (
        By.XPATH,
        "//button[text()='Войти']"
    )
