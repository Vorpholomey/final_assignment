from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") 

class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME =  (By.TAG_NAME, "h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6:nth-child(2) > p")
    BOOK_NAME_ADD = (By.CSS_SELECTOR, ".alert-safe:nth-child(1) > .alertinner strong")
    BOOK_PRICE_ADD = (By.CSS_SELECTOR, ".alert-safe:nth-child(3) > .alertinner strong")
