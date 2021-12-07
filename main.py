from selenium import webdriver
from swaglabs.ExtractData import ExtractData
from swaglabs import Login
from models import SwagBotModel

class Main:
    def __init__(self, user, password):
        self._driver = None
        self._user = user
        self._password = password
        self._login = Login.Login
        self._extract_data = ExtractData()
        self._db_model = SwagBotModel.SwagBot()

    def start(self):
        self._driver = webdriver.Chrome(executable_path='./webdriver/chromedriver.exe')
        self._driver.get('https://www.saucedemo.com/')
        self._driver.maximize_window()
        login_obj = self._login(driver=self._driver)

        send_user = login_obj.send_user(self._user)
        if isinstance(send_user, dict):
            self._db_model.create(send_user)
            return False

        send_password = login_obj.send_password(self._password)
        if isinstance(send_password, dict):
            self._db_model.create(send_password)
            return False

        btn_click = login_obj.send_login()
        if isinstance(btn_click, dict):
            self._db_model.create(btn_click)
            return False

        html_parser = self._extract_data.get_html(self._driver)
        if isinstance(html_parser, dict):
            self._db_model.create(html_parser)
            return False

        datas = self._extract_data.filter_html(parser=html_parser)
        for data in datas:
            self._db_model.create(data)

        self._driver.quit()

if __name__ == '__main__':
    bot = Main('standard_user', 'secret_sauce')
    bot.start()