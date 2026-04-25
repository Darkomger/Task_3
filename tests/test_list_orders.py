import allure

from pages.main_page import MainPage
from pages.list_orders_page import ListOrdersPage
from pages.profile_page import ProfilePage
from pages.history_orders_page import HistoryOrdersPage

from helpers import *
from data import Data

@allure.title('Тесты на проверку списка заказов')
@allure.description('В данном тесте проводится проверка функциональности списка заказов')

class TestListOrders:

    @allure.title('Проверка отображения деталей заказа')
    def test_get_details_order(self, driver):
        list_orders = ListOrdersPage(driver)
    
        list_orders.open_list_orders_page_url()
       
        list_orders.wait_for_list_orders_page_load()

        list_orders.click_first_order_element()

        new_visibility = list_orders.get_attribute_details_order_text('visibility')

        assert new_visibility == Data.DATA_STATUS_VISIBLE

    @allure.title('Проверка создания заказа')
    def test_create_order(self, login_to_account):
        driver = login_to_account

        # нажимаем на кнопку личный кабинет
        main_page = MainPage(driver)
        
        main_page.wait_for_main_page_load()

        main_page.drag_and_drop_ingredient()

        main_page.click_create_order_button()

        main_page.wait_for_visible_number_order()

        deafault_number = main_page.get_new_order_number_text()

        main_page.wait_for_change_count_of_orders(deafault_number)

        main_page.click_exit_modal_button()

        main_page.click_personal_acount()
        
        profile_page = ProfilePage(driver)

        profile_page.wait_for_profile_page_load()

        profile_page.click_history_orders()

        profile_page.wait_for_profile_page_element_invisible()

        history_orders_page = HistoryOrdersPage(driver)

        history_orders_page.wait_for_visible_order_number_element()

        history_number = history_orders_page.get_order_number_text()

        main_page.click_list_orders_button()

        list_orders = ListOrdersPage(driver)

        list_orders.wait_for_list_orders_page_load()

        list_number = list_orders.get_first_number_element_text()

        assert history_number == list_number

    @allure.title('Проверка увеличения счетчика заказов за все время')
    def test_increese_all_time_counter(self, login_to_account):
        driver = login_to_account

        main_page = MainPage(driver)
        
        main_page.wait_for_main_page_load()

        main_page.click_list_orders_button()

        list_orders = ListOrdersPage(driver)

        list_orders.wait_for_list_orders_page_load()

        old_all_time_counter = list_orders.get_all_time_orders_counter_text()

        main_page.click_constructor_button()

        main_page.wait_for_main_page_load()

        main_page.drag_and_drop_ingredient()

        main_page.click_create_order_button()

        main_page.wait_for_visible_number_order()

        deafault_number = main_page.get_new_order_number_text()

        main_page.wait_for_change_count_of_orders(deafault_number)

        main_page.click_exit_modal_button()

        main_page.click_list_orders_button()

        list_orders.wait_for_list_orders_page_load()

        list_orders.wait_for_change_count_of_all_time_orders(old_all_time_counter)

        new_all_time_counter = list_orders.get_all_time_orders_counter_text()

        assert old_all_time_counter < new_all_time_counter

    @allure.title('Проверка увеличения счетчика заказов за сегодня')
    def test_increese_today_counter(self, login_to_account):
        driver = login_to_account
        
        main_page = MainPage(driver)
        
        main_page.wait_for_main_page_load()

        main_page.click_list_orders_button()

        list_orders = ListOrdersPage(driver)

        list_orders.wait_for_list_orders_page_load()

        old_today_counter = list_orders.get_today_orders_counter_text()

        main_page.click_constructor_button()

        main_page.wait_for_main_page_load()

        main_page.drag_and_drop_ingredient()

        main_page.click_create_order_button()

        main_page.wait_for_visible_number_order()

        deafault_number = main_page.get_new_order_number_text()

        main_page.wait_for_change_count_of_orders(deafault_number)

        main_page.click_exit_modal_button()

        main_page.click_list_orders_button()

        list_orders.wait_for_list_orders_page_load()

        new_today_counter = list_orders.get_today_orders_counter_text()

        assert old_today_counter < new_today_counter

    @allure.title('Проверка заказов в процессе приготовления')
    def test_orders_in_progress(self, login_to_account):
        driver = login_to_account
        
        main_page = MainPage(driver)
        
        main_page.wait_for_main_page_load()

        main_page.click_constructor_button()

        main_page.wait_for_main_page_load()

        main_page.wait_for_main_page_load()

        main_page.drag_and_drop_ingredient()

        main_page.click_create_order_button()

        main_page.wait_for_visible_number_order()

        deafault_number = main_page.get_new_order_number_text()

        main_page.wait_for_change_count_of_orders(deafault_number)

        current_number_order = main_page.get_new_order_number_text()

        main_page.click_exit_modal_button()

        main_page.click_list_orders_button()

        list_orders = ListOrdersPage(driver)

        list_orders.wait_for_list_orders_page_load()

        old_in_progress_orders = list_orders.get_in_progress_orders_counter_text()

        list_orders.wait_for_change_in_progress_orders(old_in_progress_orders)

        new_in_progress_orders = list_orders.get_in_progress_orders_counter_text()

        assert current_number_order in new_in_progress_orders

