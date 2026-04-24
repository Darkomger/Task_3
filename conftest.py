import pytest
from selenium import webdriver
from helpers import generate_data_for_courier
from methods.courier_methods import CourierMeth

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
