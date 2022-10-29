from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.click_the_add_to_cart_button()


    def should_be_login_url(self):
        assert "/?promo=newYear" in self.browser.current_url, "?promo=newYear is absent in current url"

    def click_the_add_to_cart_button(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        title = self.browser.find_element(*ProductPageLocators.TITLE_BOOK)
        title_basket = self.browser.find_element(*ProductPageLocators.TITLE_PRODUCT_BASKET)
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_BASKET)

        assert title.text == title_basket.text, "The names don't match"
        assert price.text == price_basket.text, "The price does not match"

    def add_to_cart_button(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON)
        button.click()

    # should_not_be_success_message – не должно быть сообщения об успехе
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "A message about adding an item to the cart is displayed"
    # Отображается сообщение о добавлении товара в корзину

    # element does not disappear – элемент не исчезает
    def element_does_not_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Message did not disappear after adding the product to the cart"
    # Сообщение не исчезло после добавления товара

    def the_basket_is_empty(self):  # проверка, что корзина пуста
        assert 'empty' in self.browser.find_element(By.CSS_SELECTOR, 'p').text


