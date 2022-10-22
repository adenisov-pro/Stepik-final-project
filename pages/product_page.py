from .base_page import BasePage
from .locators import ProductPageLocators

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

