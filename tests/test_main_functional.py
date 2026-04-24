import allure

from pages.main_page import MainPage
from pages.list_orders_page import ListOrdersPage

from helpers import *

from data import Data
from urls import Urls

@allure.title('Тесты на проверку основной функциональности')
@allure.description('В данном тесте проводится проверка основной функциональности приложения')

class TestMainFunctional:

    @allure.title('Проверка перехода в конструктор')
    #@pytest.mark.parametrize('num', [0, 1])
    def test_click_constructor(self, driver):
        list_orders = ListOrdersPage(driver)
    
        list_orders.open_list_orders_page_url()
       
        list_orders.wait_for_list_orders_page_load()

        main_page = MainPage(driver)

        main_page.click_constructor_button()

        main_page.wait_for_main_page_load()

        assert main_page.get_current_url() == Urls.START_URL

    @allure.title('Проверка перехода в ленту заказов')
    def test_click_list_orders(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page_url()
        
        main_page.wait_for_main_page_load()
        
        main_page.click_list_orders_button()

        list_orders = ListOrdersPage(driver)

        list_orders.wait_for_list_orders_page_load()

        assert list_orders.get_current_url() == Urls.LIST_ORDERS_URL

    @allure.title('Проверка отображения деталей ингредиента')
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page_url()
        
        main_page.wait_for_main_page_load()
        
        main_page.click_any_burger_ingredient()
        
        main_page.wait_for_visible_details_ingredient()

        details_text = main_page.get_details_text()
        assert details_text == Data.DATA_BURGER_NAME

    @allure.title('Проверка закрытия модального окна')
    def test_click_exit_modal_button(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page_url()
        
        main_page.wait_for_main_page_load()
        
        main_page.click_any_burger_ingredient()
        
        main_page.wait_for_visible_details_ingredient()

        main_page.click_exit_modal_button()

        main_page.wait_for_exit_modal_button_invisible

        current_visibility = main_page.get_attribute_exit_button('visibility')
        #Ожидаем смену цвета границы элемента
        main_page.wait_for_change_attribute_exit_button('visibility',current_visibility)

        new_visibility = main_page.get_attribute_exit_button('visibility')

        assert new_visibility == Data.DATA_STATUS_HIDDEN

    @allure.title('Проверка увеличения счетчика ингредиента')
    def test_increese_counter_ingredient(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page_url()
        
        main_page.wait_for_main_page_load()

        current_counter =  main_page.get_counter_flu_burger_text()

        main_page.drag_and_drop_ingredient()

        #main_page.wait_for_main_page_element_invisible()

        new_counter =  main_page.get_counter_flu_burger_text()
        
        assert current_counter < new_counter

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order(self, driver, create_courier_and_delete):

        login_to_account(driver, create_courier_and_delete)
        # нажимаем на кнопку личный кабинет
        main_page = MainPage(driver)

        current_visibility = main_page.get_attribute_cooking_order('visibility')

        main_page.click_create_order_button()

        main_page.wait_for_change_attribute_order_is_cooking('visibility',current_visibility)

        new_visibility = main_page.get_attribute_cooking_order('visibility')

        assert new_visibility == Data.DATA_STATUS_VISIBLE