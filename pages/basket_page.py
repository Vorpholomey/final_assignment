from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators




class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "The basket is not empty "

    
    def should_be_message_that_basket_is_empty(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY), "The basket is not empty "

