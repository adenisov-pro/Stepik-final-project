from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    # должна быть страница входа в систему
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # должен быть URL-адрес входа в систему
    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "login is absent in current url"

    # должна быть форма входа в систему
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    # должна быть регистрационная форма
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), " Register form is not presented"

    def register_new_user(self, email_value, password_value):
        # 1) Получить доступ к полю ввода емэйла
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        # 2) Ввести значение емэйла в поле
        input_email.send_keys(email_value)

        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        input_password.send_keys(password_value)

        input_password_2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        input_password_2.send_keys(password_value)

        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()
