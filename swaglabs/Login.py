from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException


class Login:
    def __init__(self, driver):
        self._driver = driver


    def send_user(self, user):
        user = str(user)
        try:
            username = WebDriverWait(self._driver, 10).until(ec.presence_of_element_located((By.ID, 'user-name')))
            username.send_keys(user)
            return True
        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
            return {'error': True, 'data': 'Erro ao preencher usuário.'}

    def send_password(self, password):
        password = str(password)
        try:
            pwd = WebDriverWait(self._driver, 10).until(ec.presence_of_element_located((By.ID, 'password')))
            pwd.send_keys(password)
            return True
        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
            return {'error': True, 'data': 'Erro ao preencher senha.'}

    def send_login(self):
        try:
            login_button = WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable((By.ID, 'login-button')))
            login_button.click()
            return True
        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
            return {'error': True, 'data': 'Erro ao logar.'}
