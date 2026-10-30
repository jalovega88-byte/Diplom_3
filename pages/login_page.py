import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step("Ввод email пользователя")
    def enter_email(self, email):
        self.enter_text(
            LoginPageLocators.EMAIL_INPUT,
            email
        )

    @allure.step("Ввод пароля пользователя")
    def enter_password(self, password):
        self.enter_text(
            LoginPageLocators.PASSWORD_INPUT,
            password
        )

    @allure.step("Нажатие на кнопку входа")
    def click_login(self):
        self.click_element(
            LoginPageLocators.LOGIN_SUBMIT_BUTTON
        )

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()