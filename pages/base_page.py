from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import math
from .locators import BasePageLocators



class BasePage:

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 2).until(ec.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        # time.sleep(2)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()

        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):  # is_not_element_present – отсутствует элемент
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):   # is_disappeared – исчез
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # перейдите на страницу входа в систему
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        assert "/accounts/login" in self.browser.current_url, "/accounts/login is absent in current url"

    # должна быть ссылка для входа в систему
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        # Ссылка для входа в систему не представлена

    # метод перехода в корзину
    def method_of_going_to_the_cart(self):  # кнопка просмотра корзины
        button = self.browser.find_element(*BasePageLocators.VIEW_THE_SHOPPING_CART)
        button.click()
        assert "/basket" in self.browser.current_url, "basket is absent in current url"

    # метод перехода на страницу входа в систему
    def go_to_the_login_page(self):
        button = self.browser.find_element(*BasePageLocators.LOG_IN_TO_THE_SYSTEM)
        button.click()
        assert "/accounts/login" in self.browser.current_url, "/accounts/login is absent in current url"

    # должен быть авторизованным пользователем
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
        # значок пользователя не отображается\вероятно неавторизованный пользователь

