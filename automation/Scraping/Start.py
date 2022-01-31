from utils.Proppertys import Proppertys
from utils.Driver.ConfigDriver import ConfigDriver
from models import ScrapingModel, ScrapingErrosModel
from .Steps import Steps


class ScrapinUsers(Proppertys.Proppertys):
    def __init__(self):
        super().__init__()
        self._config_driver = ConfigDriver()
        self._driver = None
        self._steps = Steps()
        self._db_errors = ScrapingErrosModel.Errors()
        self._db_scraping = ScrapingModel.ScrapingBot()

    def start(self):
        self._driver = self._config_driver.set_driver()
        if isinstance(self._driver, dict):
            try:
                self._db_errors.create(self._driver)
            except:
                pass
            raise ConnectionError('Erro ao iniciar navegador')

        self._driver.get(self.url)
        self._driver.maximize_window()

        num_page = self._steps.get_max_pages(self._driver)

        if isinstance(num_page, dict):
            self._db_errors.create(num_page)
            raise ValueError('Erro ao coletar maxpage')
        elif str(num_page).isnumeric():
            max_page = int(num_page)
        else:
            self._db_errors.create(num_page)
            raise ValueError('Erro ao coletar maxpage')

        for page in range(1, max_page + 1):
            self.url = f'https://automacaocombatista.herokuapp.com/users?page={page}'
            self._driver.get(self.url)
            info = self._steps.get_info(self._driver)
            if isinstance(info, dict):
                info['page'] = self.url
                self._db_errors.create(info)
                raise ValueError(f'Erro ao coletar dados da página {page}')

        self._driver.quit()
