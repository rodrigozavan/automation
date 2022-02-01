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
        self._methods = None

        self._methods = {
            'links': {
                'method': self.links,
                'link': 'https://automacaocombatista.herokuapp.com/buscaelementos/links'
            },
            'inputs': {
                'method': self.inputs,
                'link': 'https://automacaocombatista.herokuapp.com/buscaelementos/inputsetextfield'
            },
            'buttons': {
                'method': self.buttons,
                'link': 'https://automacaocombatista.herokuapp.com/buscaelementos/botoes',
            },
            'radio_checks': {
                'method': self.radio_checks,
                'link': 'https://automacaocombatista.herokuapp.com/buscaelementos/radioecheckbox'
            },
            'dropdown': {
                'method': self.dropdown,
                'link': 'https://automacaocombatista.herokuapp.com/buscaelementos/dropdowneselect'
            },
            'text': {
                'method': self.text,
                'link': 'https://automacaocombatista.herokuapp.com/buscaelementos/textos'
            },
            'table': {
                'method': self.table,
                'link': 'https://automacaocombatista.herokuapp.com/buscaelementos/table'
            }
        }

    def start(self):

        self._driver = self._config_driver.set_driver(name='firefox')
        if isinstance(self._driver, dict):
            try:
                self._db_errors.create(self._driver)
            except:
                pass
            raise ConnectionError('Erro ao iniciar navegador')

        self._driver.get(self._methods[self.type_bot]['link'])

        function_bot = self._methods[self.type_bot]['method']
        function_bot()

        self._driver.quit()

    def links(self):
        self._steps.search_sucess(self._driver)
        self._driver.back()

    def inputs(self):
        self._steps.search_inputs(self._driver)

    def buttons(self):
        pass

    def radio_checks(self):
        pass

    def dropdown(self):
        pass

    def text(self):
        pass

    def table(self):
        pass


if __name__ == '__main__':
    bot = Start()
    bot.type_bot = 'inputs'
    bot.start()
