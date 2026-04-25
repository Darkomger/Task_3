import random
import string
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import Data

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))

    return random_string

def generate_random_email():
    username_length = random.randint(8, 12)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    
    domains = ["ya.ru","gmail.com", "yahoo.com", "outlook.com", "example.ru", "test.net"]
    domain = random.choice(domains)
    
    email = f"{username}@{domain}"
    return email

def generate_data_for_courier():

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    email = generate_random_email()
    password = generate_random_string(10)
    name = generate_random_string(10)

    login_pass.append(email)
    login_pass.append(password)
    login_pass.append(name)

    return login_pass

