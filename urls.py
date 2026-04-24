class Urls:
    START_URL = "https://stellarburgers.education-services.ru/"
    LOGIN_URL = "https://stellarburgers.education-services.ru/login"
    FORGOT_PASSWORD_URL = "https://stellarburgers.education-services.ru/forgot-password"
    RESET_PASSWORD_URL = "https://stellarburgers.education-services.ru/reset-password"
    HISTORY_ORDERS_URL = "https://stellarburgers.education-services.ru/account/order-history"
    PROFILE_URL = "https://stellarburgers.education-services.ru/account/profile"
    LIST_ORDERS_URL = "https://stellarburgers.education-services.ru/feed"

class ApiEndpoints:
    USERS_LOGIN_IN_THE_SYSTEM_ENDPOINT = "api/auth/login" # Courier - Логин курьера в системе
    CREATING_USER_ENDPOINT = "api/auth/register" # Courier - Создание курьера
    DELETING_USER_ENDPOINT = "api/auth/user" # Courier - Удаление курьера

class TotalUrl:
    CREATE_USER_URL = Urls.START_URL + ApiEndpoints.CREATING_USER_ENDPOINT # Создание курьера
    LOGIN_IN_THE_SYSTEM_URL = Urls.START_URL + ApiEndpoints.USERS_LOGIN_IN_THE_SYSTEM_ENDPOINT # Получаем логин и id user
    DELETE_USER_URL = Urls.START_URL +ApiEndpoints.DELETING_USER_ENDPOINT # Удаление курьера