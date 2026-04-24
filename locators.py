from selenium.webdriver.common.by import By

class StarterPageLocators: # Стартовая страница
    LOGIN_IN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    CONTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    LIST_ORDERS_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    MAIN_PAGE_TEXT = (By.XPATH, ".//h1[text()='Соберите бургер']")
    FLU_BREAD_BURGER_INGREDIENT = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/..")
    FLU_BREAD_BURGER_COUNTER = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/../div/p[contains(@class, 'counter')]")
    DETAILS_ANY_INGREDIENT_TEXT = (By.XPATH, ".//h2[text()='Детали ингредиента']/../p")
    EXIT_MODAL_BUTTON = (By.XPATH, ".//button[contains(@class, 'modal__close')]")
    TARGET_DRAG_FIELD = (By.XPATH, ".//ul[contains(@class, '_basket__list_')]")
    NEW_ORDER_NUMBER_FIELD = (By.XPATH, ".//p[text()='идентификатор заказа']/../h2")
    ORDER_IS_COOKING = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
class HistoryOrdersPageLocators:
    ORDER_NUMBER = (By.XPATH, ".//p[contains(text(), '#')]")
class LoginPageLocators: # Страница логина
    RECOVER_PASSWORD_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    EMAIL_FILED = (By.XPATH, ".//input[@type='text']")
    PASSWORD_FILED = (By.XPATH, ".//input[@type='password']")
class ListOrdersPageLocators: # Страница логина
    LIST_ORDERS_TEXT = (By.XPATH, ".//h1[text()='Лента заказов']")
    FIRST_ORDER_ELEMENT = (By.XPATH, ".//a[contains(@class,'OrderHistory')]")
    DETAILS_ORDER_TEXT = (By.XPATH, ".//p[text()='Cостав']")
    FIRST_NUMBER_TEXT = (By.XPATH, ".//p[contains(@class, 'text_type_digits') and not(contains(@class, 'm'))]")
    ALL_TIME_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время:']/../p[contains(@class, 'number')]")
    TODAY_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/../p[contains(@class, 'number')]")
    IN_PROGRESS_ORDERS_COUNTER = (By.XPATH, ".//ul[contains(@class, 'orderListReady')]")
class ProfilePageLocators: # Страница логина
    HISTORY_ORDERS_BUTTON = (By.XPATH, ".//a[text()='История заказов']")
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
class ForgotPasswordPageLocators: # Страница забытого пароля
    FORGOT_PASSWORD_PAGE_TEXT = (By.XPATH, ".//button[text()='Восстановить']")
    ENTER_EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/../input")
    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
class ResetPasswordPageLocators: # Страница восстановления пароля
    RESET_PASSWORD_PAGE_TEXT = (By.XPATH, ".//label[text()='Введите код из письма']")
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, ".//label[text()='Пароль']/../div/*")
    LUMINOUS_BORDER = (By.XPATH, ".//input[@type='text' and @name='Введите новый пароль']/..")