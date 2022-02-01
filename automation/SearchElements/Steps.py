from utils.Waits import Waits
import faker
from time import sleep


class Steps:

    def __init__(self):
        self._waits = Waits.Wait()
        self._SUCESS_LINK = ('css selector', 'a[href="/buscaelementos/success"]')
        self._BAD_REQUEST = ('css selector', 'a[href="/buscaelementos/badrequest"]')
        self._PAGE_NOT_FOUND = ('css selector', 'a[href="/buscaelementos/notfound"]')
        self._SERVER_ERROR = ('css selector', 'a[href="/buscaelementos/internalservererror"]')
        self._TITLE = ('css selector', 'h5.text-darken-1')
        self._INPUT_FIRST_NAME = ('css selector', 'input[id="first_name"]')
        self._INPUT_LAST_NAME = ('css selector', 'input[id="last_name"]')
        self._INPUT_PASSWORD = ('css selector', 'input[id="password"]')
        self._INPUT_EMAIL = ('css selector', 'input[id="email"]')
        self._INPUT_TEXT_AREA = ('css selector', 'textarea[id="textarea1"]')
        self._faker = faker.Faker('pt_BR')

    def search_sucess(self, driver):
        try:
            sucess = self._waits.wait_by_clickable(driver, self._SUCESS_LINK, 10)
            sucess.click()
            title = self._waits.wait_by_presence(driver, self._TITLE, 10)
            return str(title.text)
        except:
            return None

    def search_bad_request(self, driver):
        try:
            bad_request = self._waits.wait_by_clickable(driver, self._BAD_REQUEST, 10)
            bad_request.click()
            title = self._waits.wait_by_presence(driver, self._TITLE, 10)
            return str(title.text)
        except:
            return None

    def search_page_not_found(self, driver):
        try:
            page_not_found = self._waits.wait_by_clickable(driver, self._PAGE_NOT_FOUND, 10)
            page_not_found.click()
            title = self._waits.wait_by_presence(driver, self._TITLE, 10)
            return str(title.text)
        except:
            return None

    def search_server_error(self, driver):
        try:
            server_error = self._waits.wait_by_clickable(driver, self._SERVER_ERROR, 10)
            server_error.click()
            title = self._waits.wait_by_presence(driver, self._TITLE, 10)
            return str(title.text)
        except:
            return None

    def search_inputs(self, driver):
        try:
            input_first_name = self._waits.wait_by_clickable(driver, self._INPUT_FIRST_NAME, 10)
            input_last_name = self._waits.wait_by_clickable(driver, self._INPUT_LAST_NAME, 10)
            input_password = self._waits.wait_by_clickable(driver, self._INPUT_PASSWORD, 10)
            input_email = self._waits.wait_by_clickable(driver, self._INPUT_EMAIL, 10)
            input_text_area = self._waits.wait_by_clickable(driver, self._INPUT_TEXT_AREA, 10)

            elements = {
                'first_name': input_first_name,
                'last_name': input_last_name,
                'password': input_password,
                'email': input_email,
                'text_area': input_text_area
            }

            info = {
                'first_name': self._faker.first_name(),
                'last_name': self._faker.last_name(),
                'password': self._faker.last_name(),
                'email': self._faker.email(),
                'text_area': 'Teste',
            }

            for key in elements:
                elements[key].send_keys(info[key])
                sleep(1)

            return elements
        except:
            return None
