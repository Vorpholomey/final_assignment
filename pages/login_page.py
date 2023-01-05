from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL form is not presented"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        email_item = self.browser.find_element(*LoginPageLocators.EMAIL_ITEM)
        email_item.send_keys(email)
        password_item1 = self.browser.find_element(*LoginPageLocators.PASSWORD_ITEM1)
        password_item1.send_keys(password)
        password_item2 = self.browser.find_element(*LoginPageLocators.PASSWORD_ITEM2)
        password_item2.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button_registration.click() 