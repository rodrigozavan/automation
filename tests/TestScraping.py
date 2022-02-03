import unittest
from utils.Driver import ConfigDriver
from selenium.webdriver.chrome.webdriver import WebDriver


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = ConfigDriver.ConfigDriver().set_driver()
        self.driver.get("https://automacaocombatista.herokuapp.com/users")

    def test_if_init_browser(self):
        self.assertIsInstance(self.driver, WebDriver)  # add assertion here

    def test_title_contains_automacao_com_batista(self):
        title = self.driver.title
        self.assertIn('Automação com Batista', title)

    def test_if_you_are_on_the_users_page(self):
        title_users = self.driver.find_element_by_css_selector('div.tamanhodiv2 h5').text
        self.assertIn('Lista de Usuários!!', title_users)

    def test_get_last_page(self):
        element = self.driver.find_element_by_class_name('last')
        href = element.find_element_by_tag_name('a').get_attribute('href')
        maxpage = str(href).split('page')[1]
        maxpage = int(maxpage.replace('=', ''))
        self.assertIsInstance(maxpage, int)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
