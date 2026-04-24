import allure

from locators import ResetPasswordPageLocators
from pages.base_page import BasePage
from urls import Urls

class ResetPasswordPage(BasePage):
    show_hide_password_button = ResetPasswordPageLocators.SHOW_HIDE_PASSWORD_BUTTON
    luminous_border = ResetPasswordPageLocators.LUMINOUS_BORDER
    reset_password_page_text = ResetPasswordPageLocators.RESET_PASSWORD_PAGE_TEXT

    @allure.step('Переходим по ссылке на страницу')
    def open_reset_password_page_url(self):
        self.open_url(Urls.RESET_PASSWORD_URL)

    @allure.step('Ждём загрузку страницы')
    def wait_for_reset_password_page_load(self):
        self.wait_for_element_visible(self.reset_password_page_text)

    @allure.step('Кликаем по кнопке скрыть/отобразить пароль')
    def click_show_hide_password_button(self):
        self.wait_for_element_clickable(self.show_hide_password_button)
        self.click_element(self.show_hide_password_button)

    @allure.step('Получаем атрибут границы')
    def get_luminous_border_attribute(self, attribute):
        border = self.get_css_property(self.luminous_border, attribute)
        return border
    @allure.step('Ждем смену цвета границы')
    def wait_for_change_border_attridute(self,attribute,border_old):
        self.wait_for_css_property_change(self.luminous_border, attribute, border_old)
