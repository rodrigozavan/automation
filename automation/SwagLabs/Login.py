from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from utils.Waits import Waits


class Login:
    def __init__(self, driver):
        self._driver = driver
        self._wait = Waits.Wait()


    def send_user(self, user):
        user = str(user)
        try:
            username = self._wait.wait_by_presence(driver=self._driver, time=10, element=('id', 'user-name'))

            if not username:
                return {'error': True, 'data': 'Erro ao preencher usuário.', 'type': f'Elemento não encontrado',
                        'method': 'send_user'}
            else:
                username.send_keys(user)
                return True

        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException) as e:
            return {'error': True, 'data': 'Erro ao preencher usuário.', 'type': f'{e}', 'method': 'send_user'}


    def send_password(self, password):
        password = str(password)
        try:

            pwd = self._wait.wait_by_presence(driver=self._driver, time=10, element=('id', 'password'))

            if not pwd:
                return {'error': True, 'data': 'Erro ao preencher senha.', 'type': f'Elemento não encontrado',
                        'method': 'send_password'}
            else:
                pwd.send_keys(password)
                return True

        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException) as e:
            return {'error': True, 'data': 'Erro ao preencher senha.', 'type': f'{e}', 'method': 'send_password'}


    def send_login(self):
        try:

            login_button = self._wait.wait_by_presence(driver=self._driver, time=10, element=('id', 'login-button'))

            if not login_button:
                return {'error': True, 'data': 'Erro ao logar.', 'type': f'Erro não encontrado',
                        'method': 'send_login'}
            else:
                login_button.click()

                msg_error = self._wait.wait_by_presence(driver=self._driver, time=1,
                                                        element=('css selector', '[data-test="error"]'))

                if not msg_error:
                    return True
                else:
                    return {'error': True, 'data': 'Erro ao logar.', 'type': f'{msg_error.text}',
                            'method': 'send_login'}

        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException) as e:
            return {'error': True, 'data': 'Erro ao logar.', 'type': f'{e}', 'method': 'send_login'}
