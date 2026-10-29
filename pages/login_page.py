
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def enter_email(self, email):
        email_input = self.find_element(
            LoginPageLocators.EMAIL_INPUT
        )
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.find_element(
            LoginPageLocators.PASSWORD_INPUT
        )
        password_input.send_keys(password)

    def click_login(self):
        self.click_element(
            LoginPageLocators.LOGIN_SUBMIT_BUTTON
        )

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
