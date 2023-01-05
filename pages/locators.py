from selenium.webdriver.common.by import By


class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") 
    EMAIL_ITEM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_ITEM1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_ITEM2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME =  (By.TAG_NAME, "h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6:nth-child(2) > p")
    BOOK_NAME_ADD = (By.CSS_SELECTOR, ".alert-safe:nth-child(1) > .alertinner strong")
    BOOK_PRICE_ADD = (By.CSS_SELECTOR, ".alert-safe:nth-child(3) > .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-safe:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")



