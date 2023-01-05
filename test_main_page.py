
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.locators import LoginPageLocators
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()      # проверяем, что есть ссылка, которая ведет на логин 
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_register_login_form_and_link(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.should_be_register_form()
    page.should_be_login_url()



def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/" 
    page = BasePage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      #Гость открывает главную страницу 
    page.go_to_basket_page() #Переходит в корзину по кнопке в шапке
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket() #Ожидаем, что в корзине нет товаров
    basket_page.should_be_message_that_basket_is_empty() #Ожидаем, что есть текст о том что корзина пуста 







