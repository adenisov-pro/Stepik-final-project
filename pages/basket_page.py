from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def the_basket_is_empty(self):  # проверка, что корзина пуста
        assert 'empty' in self.browser.find_element(By.CSS_SELECTOR, 'p').text

    # should_not_be_success_message – не должно быть сообщения об успехе
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasePageLocators.SUCCESS_MESSAGE), \
            "A message about adding an item to the cart is displayed"
        # Отображается сообщение о добавлении товара в корзину

    # увидеть ссылку для входа в систему
    def see_the_login_link(self):
        button = self.browser.find_element(*BasePageLocators.ENTRANCE)
        button.click()
        message = self.browser.find_element(By.CSS_SELECTOR, "form#login_form h2")
        message_text = message.text
        assert message_text == "Log In", "The login link is not visible"  # Ссылка для входа в систему не видна
