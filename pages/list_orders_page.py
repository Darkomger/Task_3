import allure

from locators import ListOrdersPageLocators
from pages.base_page import BasePage
from urls import Urls

class ListOrdersPage(BasePage):
    list_orders_text = ListOrdersPageLocators.LIST_ORDERS_TEXT
    first_order_element = ListOrdersPageLocators.FIRST_ORDER_ELEMENT
    details_order_text = ListOrdersPageLocators.DETAILS_ORDER_TEXT
    first_number_element = ListOrdersPageLocators.FIRST_NUMBER_TEXT
    all_time_orders_counter = ListOrdersPageLocators.ALL_TIME_ORDERS_COUNTER
    today_orders_counter = ListOrdersPageLocators.TODAY_ORDERS_COUNTER
    in_progress_orders_counter = ListOrdersPageLocators.IN_PROGRESS_ORDERS_COUNTER
    @allure.step('Переходим по ссылке на страницу ленты заказов')
    def open_list_orders_page_url(self):
        self.open_url(Urls.LIST_ORDERS_URL)

    @allure.step('Ждём загрузку страницы')
    def wait_for_list_orders_page_load(self):
        self.wait_for_element_visible(self.list_orders_text)
    
    @allure.step('Ждем смену аттрибута стутуса готовки заказа')
    def wait_for_change_attribute_details_oerder_text(self,attribute,attribute_old):
        self.wait_for_css_property_change(self.details_order_text, attribute, attribute_old)

    @allure.step('Ждем смену закозов в процессе')
    def wait_for_change_in_progress_orders(self,text):
        self.wait_for_text_to_change(self.in_progress_orders_counter, text)

    @allure.step('Ждем смену количества всех заказов на новый')
    def wait_for_change_count_of_all_time_orders(self,text):
        self.wait_for_text_to_change(self.all_time_orders_counter, text)

    @allure.step('Кликаем на первый заказ')
    def click_first_order_element(self):
        self.wait_for_element_clickable(self.first_order_element)
        self.click_element(self.first_order_element)
        
    @allure.step('Получаем атрибут готовки заказа')
    def get_attribute_details_order_text(self, attribute):
        exit_button = self.get_css_property(self.details_order_text, attribute)
        return exit_button
    
    @allure.step('Получаем номер заказа')
    def get_first_number_element_text(self):
        text = self.get_text(self.first_number_element)
        return text
    
    @allure.step('Получаем количество заказов за все время')
    def get_all_time_orders_counter_text(self):
        text = self.get_text(self.all_time_orders_counter)
        return text
    
    @allure.step('Получаем количество заказов за сегодня')
    def get_today_orders_counter_text(self):
        text = self.get_text(self.today_orders_counter)
        return text
    
    @allure.step('Получаем заказы в процессе')
    def get_in_progress_orders_counter_text(self):
        text = self.get_text(self.in_progress_orders_counter)
        return text