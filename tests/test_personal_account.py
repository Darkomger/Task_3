import allure

from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage

from helpers import *

from urls import Urls

@allure.title('Тесты на проверку личного кабинета')
@allure.description('В данном тесте проводится проверка функциональности личного кабинета')

class TestPersonalAccount:

    @allure.title('Проверка персонального аккаунта')
    def test_click_personal_acount(self, login_to_account):
        driver = login_to_account

        main_page = MainPage(driver)
        # нажимаем на кнопку личный кабинет
        main_page.click_personal_acount()

        profile_page = ProfilePage(driver)

        profile_page.wait_for_profile_page_load()

        assert main_page.get_current_url() == Urls.PROFILE_URL

    @allure.title('Проверка перехода в историю заказов')
    def test_click_history_orders(self, login_to_account):
        driver = login_to_account
        # нажимаем на кнопку личный кабинет
        main_page = MainPage(driver)

        main_page.click_personal_acount()
        
        profile_page = ProfilePage(driver)

        profile_page.wait_for_profile_page_load()

        profile_page.click_history_orders()

        profile_page.wait_for_profile_page_element_invisible()

        assert profile_page.get_current_url() == Urls.HISTORY_ORDERS_URL

    @allure.title('Проверка выхода из аккаунта')
    def test_click_exit(self, login_to_account):
        driver = login_to_account
        # нажимаем на кнопку личный кабинет
        main_page = MainPage(driver)
        
        main_page.click_personal_acount()
        
        profile_page = ProfilePage(driver)

        profile_page.wait_for_profile_page_load()

        profile_page.click_exit_button()

        profile_page.wait_for_profile_page_element_invisible()

        assert profile_page.get_current_url() == Urls.LOGIN_URL


    