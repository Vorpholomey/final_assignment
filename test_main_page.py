#import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.locators import LoginPageLocators
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()      # проверяем, что есть ссылка, которая ведет на логин 
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_register_login_form_and_link(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.should_be_register_form()
    page.should_be_login_url()



#    page.should_be_login_link()      # проверяем, что есть ссылка, которая ведет на логин 
#    page.should_be_login_link()      # проверяем, что есть ссылка, которая ведет на логин 
#    page.should_be_login_link()      # проверяем, что есть ссылка, которая ведет на логин 
#    page.should_be_login_link()      # проверяем, что есть ссылка, которая ведет на логин 
