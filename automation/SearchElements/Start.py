from utils.Proppertys import Proppertys
from utils.Driver import ConfigDriver
from models import SerachErrors
from Steps import Steps


class Start(Proppertys.Proppertys):

    def __init__(self):
        super().__init__()
        self._steps = Steps()
        self._config_driver = ConfigDriver.ConfigDriver()
        self._driver = None
        self._db_errors = SerachErrors.Errors()

    def start(self):
        self._driver = self._config_driver.set_driver()
        if isinstance(self._driver, dict):
            try:
                self._db_errors.create(self._driver)
            except:
                pass
            raise ConnectionError('Erro ao iniciar navegador')

        self._driver.get(self.url)
        self._steps.search(self._driver)


if __name__ == '__main__':
    bot = Start()
    bot.url = 'https://automacaocombatista.herokuapp.com/buscaelementos/links'
    bot.start()
