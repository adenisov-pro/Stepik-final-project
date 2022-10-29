from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    TITLE_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRICE_PRODUCT_BASKET = (By.CSS_SELECTOR, "div.alertinner>p>strong")
    TITLE_PRODUCT_BASKET = (By.CSS_SELECTOR, "div.alertinner>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_THE_SHOPPING_CART = (By.CSS_SELECTOR, "span a.btn.btn-default")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    LOG_IN_TO_THE_SYSTEM = (By.CSS_SELECTOR, "a#login_link")
    ENTRANCE = (By.CSS_SELECTOR, "form#login_form h2")
    ENTER = "form#login_form h2"
