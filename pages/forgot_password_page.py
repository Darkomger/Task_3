import allure

from locators import ForgotPasswordPageLocators
from pages.base_page import BasePage

from urls import Urls

class ForgotPasswordPage(BasePage):
    email_field = ForgotPasswordPageLocators.ENTER_EMAIL_FIELD
    recover_button = ForgotPasswordPageLocators.RECOVER_BUTTON
    forgot_password_page_text = ForgotPasswordPageLocators.FORGOT_PASSWORD_PAGE_TEXT

    @allure.step('Кликаем по кнопке восстановить')
    def click_recover_button(self):
        self.click_element(self.recover_button)

    @allure.step('Переходим по ссылке на страницу')
    def open_forgot_password_page_url(self):
        self.open_url(Urls.FORGOT_PASSWORD_URL)

    @allure.step('Ждём загрузку страницы')
    def wait_for_forgot_password_page_load(self):
        self.wait_for_element_visible(self.forgot_password_page_text)

    @allure.step('Ждём смены страницы')
    def wait_for_forgot_password_page_element_invisible(self):
        self.wait_for_element_invisible(self.forgot_password_page_text)