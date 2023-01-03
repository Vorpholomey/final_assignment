from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
#from .locators import MainPageLocators
#from .locators import LoginPageLocators
from .locators import ProductPageLocators
#from .login_page import LoginPage


class ProductPage(BasePage):
    def add_button_click(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()


    def сompare_book_name(self):
        first_book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        second_book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADD)
        assert first_book_name.text == second_book_name.text, "Book name is different"

    def сompare_book_price(self):
        first_book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        second_book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ADD)
        assert first_book_price.text == second_book_price.text, "Book price is different"
    
    
