import allure

from locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls
from pages.main_page import MainPage

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

    @allure.step('Вход в аккаунт')
    def login_to_account(driver, create_courier_and_delete):
        # создай объект класса логина страницы приложения
        main_page = MainPage(driver)
        # перешли на страницу тестового приложения
        main_page.open_main_page_url()
        # дождись загрузки главной страницы
        main_page.wait_for_main_page_load()
        # нажимаем на кнопку личный кабинет
        main_page.click_personal_acount()
        # дождись исчезания страницы
        main_page.wait_for_main_page_element_invisible()

        login_page = LoginPage(driver)

        data = create_courier_and_delete

        login_page.input_email_field(data[0])

        login_page.input_password_field(data[1])

        login_page.click_login_button()
    
        # дождись загрузки главной страницы
        main_page.wait_for_main_page_load()