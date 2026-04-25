import allure

from locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls

class LoginPage(BasePage):
    recover_password = LoginPageLocators.RECOVER_PASSWORD_BUTTON
    login_button = LoginPageLocators.LOGIN_BUTTON
    email_filed = LoginPageLocators.EMAIL_FILED
    password_field = LoginPageLocators.PASSWORD_FILED

    @allure.step('Кликаем по кнопке восстановить пароль')
    def click_recover_password(self):
        self.click_element(self.recover_password)

    @allure.step('Переходим по ссылке на страницу')
    def open_login_page_url(self):
        self.open_url(Urls.LOGIN_URL)

    @allure.step('Кликаем по кнопке войти')
    def click_login_button(self):
        self.click_element(self.login_button)

    @allure.step('Ждём загрузку страницы')
    def wait_for_login_page_load(self):
        self.wait_for_element_visible(self.login_button)

    @allure.step('Ждём смены страницы')
    def wait_for_login_page_element_invisible(self):
        self.wait_for_element_invisible(self.login_button)

    @allure.step('Пишем в поле email')
    def input_email_field(self, text):
        self.send_text(self.email_filed, text)
    
    @allure.step('Пишем в поле password')
    def input_password_field(self, text):
        self.send_text(self.password_field, text)

