# pytest -s test_product_page.py
# pytest -s -m "new" test_product_page.py
# pytest -v --tb=line --language=en -m need_review test_product_page.py

import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

URL = "http://selenium1py.pythonanywhere.com"

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    time.sleep(1)
    page.should_be_login_url()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_the_add_to_cart_button()


def test_guest_can_add_product_to_basket_new(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.click_the_add_to_cart_button()


# гость должен увидеть ссылку для входа на странице продукта
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# гость может перейти на страницу входа в систему со страницы продукта
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


 # гость не может видеть товар в корзине, открытой со страницы товара
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.method_of_going_to_the_cart()  # метод перехода в корзину
    page.the_basket_is_empty()  # проверка, что корзина пуста
    page.should_not_be_success_message()  # проверка, что в корзине нет товаров


# гость не может видеть товар в корзине, открытой с главной страницы
@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.method_of_going_to_the_cart()  # метод перехода в корзину
    page.the_basket_is_empty() # проверка, что корзина пуста
    page.should_not_be_success_message() # проверка, что в корзине нет товаров


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = URL + "/accounts/login"
        page = LoginPage(browser, link)
        page.open()
        from random_word import RandomWords
        r = RandomWords()
        self.email_value = r.get_random_word() + "@fakemail.org"
        self.password_value = r.get_random_word() + "123"
        page.register_new_user(self.email_value, self.password_value)
        page.should_be_authorized_user()

    # пользователь не может увидеть сообщение об успешном завершении
    def test_user_cant_see_success_message(self, browser):
        # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        link = URL + "/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)  # инициализируем Page Object
        page.open()  # открываем страницу
        page.should_not_be_success_message()

    # тестовый_пользователь_может_добавить_товар_в_корзину
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        link = URL + "/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.click_the_add_to_cart_button()
