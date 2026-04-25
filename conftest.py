import pytest
from selenium import webdriver
from helpers import generate_data_for_courier
from methods.courier_methods import CourierMeth
from pages.main_page import MainPage
from pages.login_page import LoginPage

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")
    driver.maximize_window()  # Дополнительно максимизировать окно
    yield driver
    driver.quit()

@pytest.fixture
def create_courier_and_delete():
    """Фикстура для удаления курьера"""
    data = generate_data_for_courier()
    CourierMeth().create_user(
            data[0],
            data[1],
            data[2]
        )
    yield data
    currentcode, currentdata = CourierMeth().login_user(data[0], data[1])
    currenttoken = currentdata['accessToken']
    CourierMeth().delete_user(currenttoken)

@pytest.fixture
def login_to_account(driver, create_courier_and_delete):
        # создай объект класса логина страницы приложения
        main_page = MainPage(driver)
        # перешли на страницу тестового приложения
        main_page.open_main_page_url()
        # дождись загрузки главной страницы
        main_page.wait_for_main_page_load()
        # нажимаем на кнопку личный кабинет
        main_page.click_personal_acount()
        # дождись исчезания страницы
        main_page.wait_for_main_page_element_invisible()

        login_page = LoginPage(driver)

        data = create_courier_and_delete

        login_page.input_email_field(data[0])

        login_page.input_password_field(data[1])

        login_page.click_login_button()
    
        # дождись загрузки главной страницы
        main_page.wait_for_main_page_load()

        yield driver

        