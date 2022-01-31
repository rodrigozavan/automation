from automation.SwagLabs.ExtractData import ExtractData
from automation.SwagLabs import Login
from models import SwagBotModel, ErrorsSwag
from utils.Driver.ConfigDriver import ConfigDriver
from utils.Proppertys import Proppertys


class Start(Proppertys.Proppertys):
    def __init__(self):
        super().__init__()
        self._driver = None
        self._login = Login.Login
        self._extract_data = ExtractData()
        self._db_model = SwagBotModel.SwagBot()
        self._db_errors = ErrorsSwag.Errors()
        self._config_driver = ConfigDriver()

    def start(self):

        self._driver = self._config_driver.set_driver()
        if isinstance(self._driver, dict):
            raise ConnectionError('Erro ao iniciar navegador.')

        self._driver.get(self.url)
        self._driver.maximize_window()
        login_obj = self._login(driver=self._driver)

        send_user = login_obj.send_user(self._user)
        if isinstance(send_user, dict):
            self._db_errors.create(send_user)
            self._driver.quit()
            return False

        send_password = login_obj.send_password(self._password)
        if isinstance(send_password, dict):
            self._db_errors.create(send_password)
            self._driver.quit()
            return False

        btn_click = login_obj.send_login()
        if isinstance(btn_click, dict):
            self._db_errors.create(btn_click)
            self._driver.quit()
            return False

        html_parser = self._extract_data.get_html(self._driver)
        if isinstance(html_parser, dict):
            self._db_errors.create(html_parser)
            self._driver.quit()
            return False

        datas = self._extract_data.filter_html(parser=html_parser)
        for data in datas:
            self._db_model.create(data)

        self._driver.quit()


if __name__ == '__main__':
    bot = Start()
    bot.url = 'https://www.saucedemo.com/'
    bot.user = 'standard_user'
    bot.password = 'secret_sauce'
    bot.start()
