from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.INSERT_EMAIL)
        input_passw_1 = self.browser.find_element(*LoginPageLocators.INSERT_PASSWORD_1)
        input_passw_2 = self.browser.find_element(*LoginPageLocators.INSERT_PASSWORD_2)
        input_email.send_keys(email)
        input_passw_1.send_keys(password)
        input_passw_2.send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REG).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'invalid URL'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form missing'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register form missing'
