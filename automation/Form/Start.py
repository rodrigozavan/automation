from utils.Driver.ConfigDriver import ConfigDriver
from utils.Proppertys import Proppertys
from models import FormsModel, FormsErrosModel
from Steps import Steps


class Start(Proppertys.Proppertys):
    def __init__(self):
        super().__init__()
        self._driver = None
        self._config_driver = ConfigDriver()
        self._steps = Steps()
        self._db_errors = FormsErrosModel.Errors()
        self._db_data = FormsModel.FormsData()

    def start(self):
        self._driver = self._config_driver.set_driver()
        if isinstance(self._driver, dict):
            raise ConnectionError('Erro ao iniciar navegador.')

        self._driver.get(self.url)
        self._driver.maximize_window()

        elements = self._steps.get_elements(self._driver)
        if 'error' in elements:
            self._db_errors.create(elements)
            self._driver.quit()
            return False

        infos = self._steps.send_info(elements, self._driver)
        if 'error' in infos:
            self._db_errors.create(infos)
            self._driver.quit()
            return False
        else:
            self._db_data.create(infos)

        self._driver.quit()


if __name__ == '__main__':
    bot = Start()
    bot.url = 'https://automacaocombatista.herokuapp.com/users/new'
    bot.start()
