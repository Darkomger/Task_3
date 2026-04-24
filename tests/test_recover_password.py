import allure

from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage

from helpers import *

from urls import Urls

@allure.title('Тесты на проверку восстановления пароля')
@allure.description('В данном тесте проводится проверка функциональности восстановления пароля')

class TestRecoverPassword:

    @allure.title('Проверка восстановления пароля')
    def test_click_recover_password(self, driver):
        # создай объект класса логина страницы приложения
        login_page = LoginPage(driver)
        # перешли на страницу тестового приложения
        login_page.open_login_page_url()
        # дождись загрузки главной страницы
        login_page.wait_for_login_page_load()
        # нажимаем на кнопку восстановить пароль
        login_page.click_recover_password()
        # дождись исчезания страницы
        login_page.wait_for_login_page_element_invisible()
        assert login_page.get_current_url() == Urls.FORGOT_PASSWORD_URL

    @allure.title('Проверка ввода email и восстановления')
    def test_input_email_and_click_recover(self, driver):

        # создай объект класса восстановления пароля страницы приложения
        forgot_password_page = ForgotPasswordPage(driver)

        # перешли на страницу тестового приложения
        forgot_password_page.open_forgot_password_page_url()

        # дождись загрузки страницы
        forgot_password_page.wait_for_forgot_password_page_load()

        # нажимаем на кнопку восстановить
        forgot_password_page.click_recover_button()

        # дождись исчезания страницы
        forgot_password_page.wait_for_forgot_password_page_element_invisible()

        assert forgot_password_page.get_current_url() == Urls.RESET_PASSWORD_URL
    @allure.title('Проверка смены цвета границы при активации поля')
    def test_switch_color_of_border_when_active(self, driver):

        # создай объект класса сбрасывания пароля страницы приложения
        reset_password_page = ResetPasswordPage(driver)
        
        # перешли на страницу тестового приложения
        reset_password_page.open_reset_password_page_url()

        # создай объект класса восстановления пароля страницы приложения
        forgot_password_page = ForgotPasswordPage(driver)

        # дождись загрузки страницы
        forgot_password_page.wait_for_forgot_password_page_load()

        # нажимаем на кнопку восстановить
        forgot_password_page.click_recover_button()

        # дождись загрузки главной страницы
        reset_password_page.wait_for_reset_password_page_load()

        # нажимаем на кнопку скрыть/отобразить пароль
        reset_password_page.click_show_hide_password_button()

        # цвет границы элемента
        current_colour = reset_password_page.get_luminous_border_attribute('border')

        assert '47, 47, 55' in current_colour

        #Ожидаем смену цвета границы элемента
        reset_password_page.wait_for_change_border_attridute('border',current_colour)

        # цвет границы элемента
        new_colour = reset_password_page.get_luminous_border_attribute('border')

        assert new_colour != current_colour
       