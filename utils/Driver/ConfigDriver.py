from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import config


class ConfigDriver:
    def __init__(self):
        self._driver = None
        self._config = config
        self._firefox_options = FirefoxOptions()
        self._chrome_options = ChromeOptions()

    def set_driver(self, name='chrome'):
        try:
            if not self._config.debug:
                self._firefox_options.add_argument('headless')
                self._chrome_options.add_argument('headless')

            if name == 'firefox':
                self._driver = webdriver.Firefox(executable_path=self._config.Firefox, options=self._firefox_options)
            else:
                self._driver = webdriver.Chrome(executable_path=self._config.Chrome, options=self._chrome_options)

            return self._driver
        except Exception as e:
            return {'error': True, 'type': 'Erro ao iniciar navegador.', 'msg': e}
