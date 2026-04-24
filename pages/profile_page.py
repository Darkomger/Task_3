import allure

from locators import ProfilePageLocators
from pages.base_page import BasePage

class ProfilePage(BasePage):
    history_orders = ProfilePageLocators.HISTORY_ORDERS_BUTTON
    save_button =  ProfilePageLocators.SAVE_BUTTON
    exit_button =  ProfilePageLocators.EXIT_BUTTON
    @allure.step('Кликаем по кнопке история заказов')
    def click_history_orders(self):
        self.click_element(self.history_orders)

    @allure.step('Кликаем по кнопке выйти')
    def click_exit_button(self):
        self.click_element(self.exit_button)

    @allure.step('Ждём загрузку страницы')
    def wait_for_profile_page_load(self):
        self.wait_for_element_visible(self.save_button)

    @allure.step('Ждём смены страницы')
    def wait_for_profile_page_element_invisible(self):
        self.wait_for_element_invisible(self.save_button)