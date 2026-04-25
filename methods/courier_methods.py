import requests
from urls import TotalUrl
import allure

class CourierMeth:
    @allure.step("Логин курьера")
    def login_user(self, email, password):
        payload = {
            "email": email, 
            "password": password
        }
        respons = requests.post(TotalUrl.LOGIN_IN_THE_SYSTEM_URL, data=payload)
        return respons.status_code, respons.json()

    @allure.step("Создание курьера")
    def create_user(self, email, password, name):
        payload = {
            "email": email, 
            "password": password, 
            "name": name
        }
        respons = requests.post(TotalUrl.CREATE_USER_URL, data=payload)
        return respons.status_code, respons.json()
    
    @allure.step("Удаление курьера")
    def delete_user(self, token):
        respons = requests.delete(f"{TotalUrl.DELETE_USER_URL}", headers={'Authorization': token})
        return respons.status_code, respons.text