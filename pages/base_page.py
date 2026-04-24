import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    @allure.step('Инициализируем драйвер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждём когда элемент станет кликабельным')
    def wait_for_element_clickable(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(element))

    @allure.step('Ждём когда элемент станет видимым')
    def wait_for_element_visible(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(element))

    @allure.step('Ждём когда элемент пропадёт')
    def wait_for_element_invisible(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(element))

    @allure.step('Ждём количество открытых окон')
    def wait_for_number_of_windows_to_be(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(element))

    @allure.step('Ждём конкретно окно')
    def wait_for_title_is(self, element):
        WebDriverWait(self.driver, 30).until(expected_conditions.title_is(element))

    def wait_for_text_to_change(self, locator, old_text):
        return WebDriverWait(self.driver, 10).until(expected_conditions.none_of(expected_conditions.text_to_be_present_in_element(locator, old_text)))

    @allure.step('Наводимся и кликаем на элемент')
    def click_element(self, element):
        current_element = self.driver.find_element(*element)
        current_element.location_once_scrolled_into_view
        actions = ActionChains(self.driver)
        actions.move_to_element(current_element).click().perform()

    @allure.step('Получаем текст элемента')
    def get_text(self, element):
        return self.driver.find_element(*element).text
    
    @allure.step('Получаем атрибут элемента')
    def get_attribute(self, element, attribute_name):
        return self.driver.find_element(*element).get_attribute(attribute_name)

    @allure.step('Получаем CSS свойство элемента')
    def get_css_property(self, element, property_name):
        return self.driver.find_element(*element).value_of_css_property(property_name)

    @allure.step('Ждём изменения CSS свойства')
    def wait_for_css_property_change(self, element, property_name, old_value):
        WebDriverWait(self.driver, 5).until(lambda driver: self.get_css_property(element, property_name) != old_value)

    @allure.step('Отправляем текст в элемент')
    def send_text(self, element, text):
        return self.driver.find_element(*element).send_keys(text)

    @allure.step('Наводимся и кликаем на элемент и выбираем нужный из dropdown')
    def click_of_dropdown_element(self, element, text):
        current_element = self.driver.find_element(*element)
        current_element.location_once_scrolled_into_view
        actions = ActionChains(self.driver)
        actions.move_to_element(current_element).click().perform()

        current_text = self.driver.find_element(*text)
        current_text.location_once_scrolled_into_view
        actions = ActionChains(self.driver)
        actions.move_to_element(current_text).click().perform()

    def drag_and_drop_element(self, locator_from, locator_to):
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
                   var source = arguments[0];
                   var target = arguments[1];
                   var evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
               """, element_from, element_to)

    @allure.step('Получаем текущий handle окна')
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step('Получаем список handles окон')
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step('Переключаемся на окно по handle')
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Открываем URL')
    def open_url(self, url):
        self.driver.get(url)
