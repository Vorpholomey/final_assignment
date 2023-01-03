#import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.locators import LoginPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_button_click()
    page.solve_quiz_and_get_code()
 #   time.sleep(2)
    page.сompare_book_name()
    page.сompare_book_price()






