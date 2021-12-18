from utils.Waits import Waits
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
import random


class Steps:
    def __init__(self):
        self._wait = Waits.Wait()
        self._faker = Faker('pt_BR')
        self._action = None

    def get_elements(self, driver):
        try:
            user_name = self._wait.wait_by_presence(driver, ('id', 'user_name'), 3)
            user_last_name = self._wait.wait_by_presence(driver, ('id', 'user_lastname'), 3)
            user_email = self._wait.wait_by_presence(driver, ('id', 'user_email'), 3)
            user_address = self._wait.wait_by_presence(driver, ('id', 'user_address'), 3)
            user_university = self._wait.wait_by_presence(driver, ('id', 'user_university'), 3)
            user_profile = self._wait.wait_by_presence(driver, ('id', 'user_profile'), 3)
            user_gender = self._wait.wait_by_presence(driver, ('id', 'user_gender'), 3)
            user_age = self._wait.wait_by_presence(driver, ('id', 'user_age'), 3)

            elements = {
                'username': user_name,
                'user_last_name': user_last_name,
                'user_email': user_email,
                'user_address': user_address,
                'user_university': user_university,
                'user_profile': user_profile,
                'user_gender': user_gender,
                'user_age': user_age,
            }

            for key in elements:
                if not elements[key]:
                    return {'error': True, 'type': f'Erro ao encontrar o elemento {key}'}
                else:
                    continue

            return elements

        except:
            return {'error': True, 'type': 'Erro ao processar elementos.'}

    def send_info(self, elements, driver):
        info = {
                'username': self._faker.first_name(),
                'user_last_name': self._faker.last_name(),
                'user_email': self._faker.email(),
                'user_address': self._faker.street_name(),
                'user_university': self._faker.country(),
                'user_profile': 'Teste',
                'user_gender': 'Teste',
                'user_age': random.randint(0, 70),
            }

        try:
            for key in elements:
                elements[key].send_keys(info[key])
        except:
            return {'error': True, 'type': 'Erro ao preencher informações'}

        btn_create = self._wait.wait_by_clickable(driver, ('css selector', '[value="Criar"]'), 10)
        if not btn_create:
            return {'error': True, 'type': 'Erro ao criar usuário'}
        else:
            try:
                self._action = ActionChains(driver)
                self._action.move_to_element(btn_create)
                btn_create.click()
                return info
            except:
                return {'error': True, 'type': 'Erro ao criar usuário'}
