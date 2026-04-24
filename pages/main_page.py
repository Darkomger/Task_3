import allure

from locators import StarterPageLocators
from pages.base_page import BasePage
from urls import Urls

class MainPage(BasePage):
    login_buttons = {
        0 : StarterPageLocators.LOGIN_IN_ACCOUNT_BUTTON,
        1 : StarterPageLocators.PERSONAL_ACCOUNT_BUTTON
    }
    constructor_button = StarterPageLocators.CONTRUCTOR_BUTTON
    list_orders_button = StarterPageLocators.LIST_ORDERS_BUTTON
    main_page_text = StarterPageLocators.MAIN_PAGE_TEXT
    exit_modal_button = StarterPageLocators.EXIT_MODAL_BUTTON
    order_is_cooking = StarterPageLocators.ORDER_IS_COOKING
    create_order_button = StarterPageLocators.CREATE_ORDER_BUTTON
    new_order_number_field = StarterPageLocators.NEW_ORDER_NUMBER_FIELD


    target_drag_field = StarterPageLocators.TARGET_DRAG_FIELD
    flu_bread_burger_ingredient = StarterPageLocators.FLU_BREAD_BURGER_INGREDIENT
    flu_bread_burger_counter = StarterPageLocators.FLU_BREAD_BURGER_COUNTER
    details_any_ingredient_text = StarterPageLocators.DETAILS_ANY_INGREDIENT_TEXT

    @allure.step('Ждём загрузки главной страницы')
    def wait_for_main_page_load(self):
        self.wait_for_element_visible(self.main_page_text)

    @allure.step('Ждём видимость ингредиента')
    def wait_for_visible_details_ingredient(self):
        self.wait_for_element_visible(self.details_any_ingredient_text)

    @allure.step('Ждём видимость номера заказа')
    def wait_for_visible_number_order(self):
        self.wait_for_element_visible(self.new_order_number_field)
    
    @allure.step('Ждём исчезновение крестика')
    def wait_for_exit_modal_button_invisible(self):
        self.wait_for_element_invisible(self.exit_modal_button)

    @allure.step('Ждём смены страницы')
    def wait_for_main_page_element_invisible(self):
        self.wait_for_element_invisible(self.login_buttons[0])
    
    @allure.step('Ждём когда ингридент станет кликабельным')
    def wait_for_exit_modal_button_invisible(self):
        self.wait_for_element_clickable(self.exit_modal_button)
    
    @allure.step('Ждем смену аттрибута крестика')
    def wait_for_change_attribute_exit_button(self,attribute,attribute_old):
        self.wait_for_css_property_change(self.exit_modal_button, attribute, attribute_old)

    @allure.step('Ждем смену аттрибута стутуса готовки заказа')
    def wait_for_change_attribute_order_is_cooking(self,attribute,attribute_old):
        self.wait_for_css_property_change(self.order_is_cooking, attribute, attribute_old)

    @allure.step('Ждем смену номера заказа но новый')
    def wait_for_change_count_of_orders(self,text):
        self.wait_for_text_to_change(self.new_order_number_field, text)

    @allure.step('Переходим по ссылке на главную страницу')
    def open_main_page_url(self):
        self.open_url(Urls.START_URL)

    @allure.step('Кликаем на любой ингредиет бургера')
    def click_any_burger_ingredient(self):
        self.wait_for_element_clickable(self.flu_bread_burger_ingredient)
        self.click_element(self.flu_bread_burger_ingredient)

    @allure.step('Кликаем на крестик')
    def click_exit_modal_button(self):
        self.wait_for_element_visible(self.exit_modal_button)
        self.wait_for_element_clickable(self.exit_modal_button)
        self.click_element(self.exit_modal_button)

    @allure.step('Кликаем на кнопку личного кабинета')
    def click_personal_acount(self):
        self.wait_for_element_clickable(self.login_buttons[1])
        self.click_element(self.login_buttons[1])

    @allure.step('Кликаем на кнопку конструктор')
    def click_constructor_button(self):
        self.wait_for_element_clickable(self.constructor_button)
        self.click_element(self.constructor_button)

    @allure.step('Кликаем на кнопку лента заказов')
    def click_list_orders_button(self):
        self.wait_for_element_clickable(self.list_orders_button)
        self.click_element(self.list_orders_button)

    @allure.step('Кликаем на кнопку оформить заказ')
    def click_create_order_button(self):
        self.wait_for_element_clickable(self.create_order_button)
        self.click_element(self.create_order_button)
    
    @allure.step('Кликаем на кнопку войти в аккаунт')
    def click_login_in_account(self):
        self.wait_for_element_clickable(self.login_buttons[0])
        self.click_element(self.login_buttons[0])

    @allure.step('Получаем текст деталей')
    def get_details_text(self):
        text = self.get_text(self.details_any_ingredient_text)
        return text
    
    @allure.step('Получаем номер заказа')
    def get_new_order_number_text(self):
        text = self.get_text(self.new_order_number_field)
        return text
    
    @allure.step('Получаем счетчик количества')
    def get_counter_flu_burger_text(self):
        text = self.get_text(self.flu_bread_burger_counter)
        return text
    
    @allure.step('Получаем атрибут крестика')
    def get_attribute_exit_button(self, attribute):
        exit_button = self.get_css_property(self.exit_modal_button, attribute)
        return exit_button
    
    @allure.step('Получаем атрибут готовки заказа')
    def get_attribute_cooking_order(self, attribute):
        exit_button = self.get_css_property(self.order_is_cooking, attribute)
        return exit_button
    
    @allure.step('Перетягиваем ингредиет в заказ')
    def drag_and_drop_ingredient(self):    
        self.drag_and_drop_element(self.flu_bread_burger_ingredient,self.target_drag_field)