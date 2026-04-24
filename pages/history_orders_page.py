import allure

from locators import HistoryOrdersPageLocators
from pages.base_page import BasePage

class HistoryOrdersPage(BasePage):

    order_number_element = HistoryOrdersPageLocators.ORDER_NUMBER
    
    @allure.step('Получаем текст деталей')
    def get_order_number_text(self):
        text = self.get_text(self.order_number_element)
        return text
    
    @allure.step('Ждём видимость номера заказа')
    def wait_for_visible_order_number_element(self):
        self.wait_for_element_visible(self.order_number_element)