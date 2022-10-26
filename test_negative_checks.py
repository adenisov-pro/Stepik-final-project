# pytest -s test_negative_checks.py
from .pages.product_page import ProductPage

# гость не может увидеть сообщение об успешном завершении после добавления товара в корзину
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object
    page.open()  # открываем страницу
    page.add_to_cart_button()
    page.should_not_be_success_message()

# гость не может увидеть сообщение об успешном завершении
def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object
    page.open()  # открываем страницу
    page.should_not_be_success_message()

# сообщение исчезло после добавления товара в корзину
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object
    page.open()  # открываем страницу
    page.add_to_cart_button()
    page.element_does_not_disappear()
